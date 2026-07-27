import requests
import json
import pandas as pd
import sqlite3
import numpy as np
from datetime import datetime, date, timedelta, timezone
from pathlib import Path
from airflow.models import DAG
from airflow.providers.standard.operators.python import PythonOperator
from airflow.sdk.exceptions import AirflowSkipException, AirflowException, AirflowFailException

centre_lat = -26.204
centre_lon = 28.0473
search_radius = 250
log_file = '/mnt/c/Users/tmagw/OneDrive/Desktop/Project/log_file.txt'
output_file = '/mnt/c/Users/tmagw/OneDrive/Desktop/Project/results.csv'

query = '''SELECT nf.date,nf.alt_baro,nf.gs,nf.ias,nf.tas,nf.mach,nf.true_heading,nf.baro_rate,nf.lat,nf.lon,nf.seen,nf.distance_frm_centre,ac.icao_id,ac.registration,md.type,md.description
            FROM normalized_flights nf
            INNER JOIN aircraft ac
            ON nf.aircraft_id = ac.aircraft_id
            INNER JOIN model md
            ON nf.model_id = md.model_id
            WHERE distance_frm_centre < 100 AND (md.description LIKE '%Boeing%' OR md.description LIKE '%Airbus%')
            ORDER BY distance_frm_centre DESC
            LIMIT 5
'''

api_url = f'https://api.airplanes.live/v2/point/{centre_lat}/{centre_lon}/{search_radius}'


def extract_data(url):
    try:
        write_log('Extraction Started')
        response = requests.get(url, timeout = 5)
        response.raise_for_status()
        df = pd.DataFrame(response.json()['ac'])
        if df.size > 0:
            df.to_csv('/mnt/c/Users/tmagw/OneDrive/Desktop/Project/source_data.csv', index = False, lineterminator='\n')
            write_log('Extraction Completed')
        else:
            write_log('No Flights Found. No Further Action')
            raise AirflowSkipException('No Flights Found. No Further Action')
    except requests.exceptions.HTTPError:
        write_log(f'Extraction Failed Due To {response.status_code}: {response.reason}')
        raise AirflowFailException(f'Extraction Failed Due To {response.status_code}: {response.reason}')

    except requests.exceptions.ConnectionError as conn_err:
        write_log(f'Extraction Failed Due To {conn_err}. Scheduled For Retry')
        raise AirflowException(f'Extraction Failed Due To {conn_err}. Scheduled For Retry')

    except requests.exceptions.Timeout as time_err:
        write_log(f'Extraction Failed Due To {time_err}. Scheduled For Retry')
        raise AirflowException(f'Extraction Failed Due To {time_err}. Scheduled For Retry')

    return

def transform_data():
    write_log('Transformation Started')
    df = pd.read_csv('/mnt/c/Users/tmagw/OneDrive/Desktop/Project/source_data.csv')
    df_filtered = df[['hex','flight', 'r', 't', 'desc', 'alt_baro', 'gs','ias', 'tas', 'mach','true_heading', 'baro_rate','lat', 'lon','seen']]
    df_filtered.rename(columns = {'desc':'description'}, inplace=True)
    df_clean = df_filtered.dropna().reset_index(drop=True)
    if df_clean.size > 0:
        df_with_dist = calculate_distance(df_clean)
        df_with_dist['date'] = date.today()
        date_col = df_with_dist.pop('date')
        df_with_dist.insert(0, 'date', date_col)
        df_with_dist.to_csv('/mnt/c/Users/tmagw/OneDrive/Desktop/Project/transformed_data.csv', index = False, lineterminator='\n')
        write_log('Transformation Completed')
    else:
        write_log('Flights Found Have Missing Data. No Further Action')
        raise AirflowSkipException('Flights Found Have Missing Data. No Further Action')

    return

def calculate_distance(cleaned_df):
    plane_lat_rad = np.radians(cleaned_df['lat'])
    plane_lon_rad = np.radians(cleaned_df['lon'])
    earth_radius_km = 6371
    centre_lat_rad = np.radians(centre_lat)
    centre_lon_rad = np.radians(centre_lon)
    cos_centre_lat = np.cos(centre_lat_rad)
    plane_cos_lat = np.cos(plane_lat_rad)
    plane_sin_lat_term = np.sin((plane_lat_rad-centre_lat_rad)/2)
    plane_sin_lon_term = np.sin((plane_lon_rad-centre_lon_rad)/2)
    plane_cos_lat = np.cos(plane_lat_rad)
    cleaned_df['distance_frm_centre'] = np.round(2*earth_radius_km*np.arcsin(np.sqrt(np.square(plane_sin_lat_term)+cos_centre_lat*plane_cos_lat*np.square(plane_sin_lon_term))),decimals=0)
   
    return cleaned_df

def load_data():
    write_log('Loading Started')
    transformed_data = pd.read_csv('/mnt/c/Users/tmagw/OneDrive/Desktop/Project/transformed_data.csv')
    conn = sqlite3.connect('/mnt/c/Users/tmagw/OneDrive/Desktop/Project/flights_tracking.db')
    transformed_data.to_sql('processed_flights',conn, if_exists='append',index=False)
    normalize_tables(conn)
    conn.commit()
    conn.close()
    write_log('Loading Completed')

    return

def write_log(message):
    with open(log_file, 'a') as out_file:
        out_file.write(f'{datetime.now()}:\t{message}\n')

    return

def database_query(query,output_file):
    write_log('Running Query')
    conn = sqlite3.connect('/mnt/c/Users/tmagw/OneDrive/Desktop/Project/flights_tracking.db')
    query_result = pd.read_sql(query,conn)
    conn.close()
    write_log('Query Output Received')
    if query_result.size > 0:
        write(query_result, output_file)
    else:
        write_log('Query Output Has No Records. No Further Action')
        raise AirflowSkipException('Query Output Has No Records. No Further Action')

    return
   

def write(query_output,output_file):
    write_log('Writing Query Result to File')
    file_path = Path(output_file)
    query_output.to_csv(output_file, mode='a', index=False, header = not file_path.is_file(), lineterminator="\n")
    write_log('Writing Completed')

    return

def normalize_tables(conn):
    cur = conn.cursor()

    cur.execute('''
    CREATE TABLE IF NOT EXISTS model(model_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, type VARCHAR(16) UNIQUE, description VARCHAR(32) UNIQUE);
        ''')

    cur.execute('''
    INSERT INTO model(type, description)SELECT DISTINCT t, description FROM processed_flights WHERE t NOT IN (SELECT type FROM model) AND description NOT IN (SELECT description FROM model);
        ''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS aircraft(aircraft_id INTEGER PRIMARY KEY AUTOINCREMENT, icao_id VARCHAR(10) UNIQUE, registration VARCHAR(10) UNIQUE, model_id INTEGER REFERENCES model(model_id))
    ''')

    cur.execute('''
    INSERT INTO aircraft(icao_id,registration,model_id)SELECT DISTINCT pf.hex, pf.r, md.model_id
    FROM processed_flights pf
    INNER JOIN model md
    ON pf.description = md.description
    WHERE pf.hex NOT IN (SELECT icao_id FROM aircraft) AND pf.r NOT IN (SELECT registration FROM aircraft)
    ''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS normalized_flights (flight_id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    alt_baro INTEGER,
    gs REAL,
    ias REAL,
    tas REAL,
    mach REAL,
    true_heading REAL,
    baro_rate REAL,
    lat REAL,
    lon REAL,
    seen REAL,
    distance_frm_centre REAL,                                        
    aircraft_id INTEGER,
    model_id INTEGER
    )
    ''')

    cur.execute('''
    INSERT INTO normalized_flights (date,alt_baro,gs,ias,tas,mach,true_heading,baro_rate,lat,lon,seen,distance_frm_centre,aircraft_id,model_id)
    SELECT pf.date,pf.alt_baro,pf.gs,pf.ias,pf.tas,pf.mach,pf.true_heading,pf.baro_rate,pf.lat,pf.lon,pf.seen,pf.distance_frm_centre,ac.aircraft_id,ac.model_id
    FROM processed_flights pf
    INNER JOIN aircraft ac
    ON pf.hex = ac.icao_id
    ''')
    
    cur.execute('''
    DROP TABLE processed_flights
    ''')
    
    return

default_args = {
    'owner': 'xxx',
    'start_date': datetime(2026, 7, 15, tzinfo = timezone(timedelta(hours = 2))),
    'retries':1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    dag_id = 'Flights_Tracking',
    default_args = default_args,
    schedule = '0 20 * * *'
)

extract_task = PythonOperator(
    task_id = 'extract',
    python_callable = extract_data,
    op_kwargs= {
        'url': api_url
    },
    dag = dag
)

transform_task = PythonOperator(
    task_id = 'transform',
    python_callable = transform_data,
    dag = dag
)

load_task = PythonOperator(
    task_id = 'load',
    python_callable = load_data,
    dag = dag
)

query_task = PythonOperator(
    task_id = 'query',
    python_callable = database_query,
    op_kwargs = {
        'query':query,
        'output_file': output_file
    },
    dag = dag
)

extract_task>>transform_task>>load_task>>query_task

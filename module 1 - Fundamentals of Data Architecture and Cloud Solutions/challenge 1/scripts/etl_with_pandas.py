# GENERAL SETTINGS --------------------------------------------------------------------------------------------------------------------
# Packages
import boto3
import pandas as pd
import os
# Paths
## Main directory
module_path = os.path.abspath(os.path.join('..'))
## raw-data directory
raw_data_path = module_path + "/bootcamp/module 1 - Fundamentals of Data Architecture and Cloud Solutions/challenge 1/data/bucket/raw-data/"
## consumer-zone directory
consumer_zone_path = module_path + "/bootcamp/module 1 - Fundamentals of Data Architecture and Cloud Solutions/challenge 1/data/bucket/consumer-zone/"
print('SUCCESS - GENERAL SETTINGS\n')

# EXTRACTION --------------------------------------------------------------------------------------------------------------------
# Client to access the Amazon S3 bucket
s3_client = boto3.client('s3')
# Download data from raw-data layer
s3_client.download_file("datalake-mascalmeida-284935897552", "raw-data/MICRODADOS_ENEM_2020.csv", raw_data_path + "MICRODADOS_ENEM_2020.csv")
# Read data after the download
df = pd.read_csv(raw_data_path + "MICRODADOS_ENEM_2020.csv", sep=';', engine="pyarrow", usecols=['TP_SEXO', 'NU_NOTA_MT', 'NU_NOTA_CH', 'SG_UF_ESC', 'CO_MUNICIPIO_ESC', 'NO_MUNICIPIO_ESC', 'CO_MUNICIPIO_PROVA', 'NO_MUNICIPIO_PROVA', 'Q008', 'Q002'])
print('SUCCESS - EXTRACTION\n')

# TRANSFORMATION --------------------------------------------------------------------------------------------------------------------
# Preprocessing
df.loc[:, 'CO_MUNICIPIO_ESC'] = df.loc[:, 'CO_MUNICIPIO_ESC'].fillna(-1)
df['CO_MUNICIPIO_ESC'] = df['CO_MUNICIPIO_ESC'].astype(int)
df['NO_MUNICIPIO_ESC'] = df['NO_MUNICIPIO_ESC'].str.decode('latin-1')
df['NO_MUNICIPIO_PROVA'] = df['NO_MUNICIPIO_PROVA'].str.decode('latin-1')
print('SUCCESS - TRANSFORMATION\n')

# LOADING --------------------------------------------------------------------------------------------------------------------
df.to_parquet(consumer_zone_path + "enem2020.parquet")
# Upload data to consumer-zone layer
s3_client.upload_file(consumer_zone_path + "enem2020.parquet", "datalake-mascalmeida-284935897552", "consumer-zone/enem2020.parquet")
print('SUCCESS - LOADING\n')
print('\n>>> ETL IS DONE <<<\n')
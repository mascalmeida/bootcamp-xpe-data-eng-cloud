# GENERAL SETTINGS --------------------------------------------------------------------------------------------------------------------
# Packages
import boto3
import pandas as pd
import os
# Paths
## Main directory
module_path = os.path.abspath(os.path.join('..'))
## consumer-zone directory
consumer_zone_path = module_path + "/bootcamp/module 1 - Fundamentals of Data Architecture and Cloud Solutions/challenge 1/data/bucket/consumer-zone/"
print('SUCCESS - GENERAL SETTINGS\n')

# CONSUMPTION --------------------------------------------------------------------------------------------------------------------
# Client to access the Amazon S3 bucket
s3_client = boto3.client('s3')
# Download data from raw-data layer
s3_client.download_file("datalake-mascalmeida-284935897552", "consumer-zone/enem2020.parquet", consumer_zone_path + "enem2020.parquet")
# Read data after the download
# PARQUET ref: https://pythonspeed.com/articles/pandas-read-csv-fast/
df = pd.read_parquet(consumer_zone_path + "enem2020.parquet", engine="fastparquet")
print('SUCCESS - CONSUMPTION\n')

# SOLUTION --------------------------------------------------------------------------------------------------------------------
# Pergunta 5 - Sobre o ENEM 2020, qual é a média da nota em matemática apenas para as alunas do sexo Feminino?
r5 = df.loc[(df['TP_SEXO'] == 'F') & (df['NU_NOTA_MT'].notnull()), 'NU_NOTA_MT'].mean()
print("\nResposta 5 =", r5)
# Pergunta 6 - Qual é a média da nota em Ciências Humanas para os alunos do sexo masculino que estudaram numa escola no estado de São Paulo?
r6 = df.loc[
    (df['TP_SEXO'] == 'M') & 
    (df['NU_NOTA_CH'].notnull()) &
    (df['SG_UF_ESC'] == 'SP'), 
    'NU_NOTA_CH'
    ].mean()
print("\nResposta 6 =", r6)
# Pergunta 7 - Qual é a média da nota em Ciências Humanas dos alunos que estudaram numa escola na cidade de Natal?
r7 = df.loc[
    (df['NU_NOTA_CH'].notnull()) &
    (df['NO_MUNICIPIO_ESC'] == 'Natal'), 
    'NU_NOTA_CH'
    ].mean()
print("\nResposta 7 =", r7)
# Pergunta 8 - Qual é o município (município da escola) que obteve a maior nota MÉDIA em matemática?
r8 = df.loc[
    (df['NU_NOTA_MT'].notnull()) &
    (df['CO_MUNICIPIO_ESC'] != -1), 
    ['CO_MUNICIPIO_ESC', 'NO_MUNICIPIO_ESC', 'NU_NOTA_MT']
    ].groupby(['CO_MUNICIPIO_ESC', 'NO_MUNICIPIO_ESC']).mean().sort_values(by='NU_NOTA_MT', ascending=False).reset_index().loc[0, 'NO_MUNICIPIO_ESC']

print("\nResposta 8 =", r8)
# Pergunta 9 - Quantas pessoas que estudaram numa escola em Recife fizeram a prova do ENEM nessa mesma cidade?
r8 = len(df.loc[(df['NO_MUNICIPIO_ESC'] == 'Recife') & (df['NO_MUNICIPIO_PROVA'] == 'Recife'), ['NO_MUNICIPIO_PROVA', 'NO_MUNICIPIO_ESC']])
print("\nResposta 9 =", r8)
# Pergunta 10 - Qual é a nota média em Ciências Humanas dos alunos que estudaram numa escola no estado de Santa Catarina e possuem PELO MENOS 1 banheiro em casa?
r10 = df.loc[
    (df['NU_NOTA_CH'].notnull()) &
    (df['SG_UF_ESC'] == 'SC') &
    (df['Q008'].isin(['B', 'C', 'D', 'E'])), 
    'NU_NOTA_CH'
    ].mean()
print("\nResposta 10 =", r10)
# Pergunta 11 - Qual é a nota média em matemática dos alunos cuja mãe possui PELO MENOS o ensino superior completo, do sexo feminino que estudaram numa escola em Belo Horizonte?
r11 = df.loc[
    (df['NU_NOTA_MT'].notnull()) &
    ((df['Q002'] == 'F') | (df['Q002'] == 'G')) &
    (df['TP_SEXO'] == 'F') &
    (df['NO_MUNICIPIO_ESC'] == 'Belo Horizonte'), 
    'NU_NOTA_MT'
    ].mean()
print("\nResposta 11 =", r11)
print('\nSUCCESS - SOLUTION\n')
print('\n>>> CONSUMPTION IS DONE <<<\n')
# GENERAL SETTINGS --------------------------------------------------------------------------------------------------------------------

# Packages
## Spark packages
import pyspark
from pyspark.sql import SparkSession
## General packages
import os

## work with pandas functions
import pyspark.pandas as ps
# Show only 20 rows with Pandas API
ps.options.display.max_rows = 20
ps.set_option('compute.ops_on_diff_frames', True)

# Paths
## Main directory
module_path = os.path.abspath(os.path.join('..'))
## enade data directory
enade_data_path = module_path + "/data/raw/enade2017/data/"
## staging data directory
staging_data_path = module_path + "/data/staging/"

# Create spark session
spark = (
    SparkSession.builder.appName("challenge2_module3")
    .getOrCreate()
)

print('SUCCESS - GENERAL SETTINGS\n')

# EXTRACTION --------------------------------------------------------------------------------------------------------------------
## Reading data from raw layer
df1_enade = spark.read.csv(enade_data_path + 'microdados2017_arq1.txt', header=True, inferSchema=True, sep=';')
pd_df1_enade = df1_enade.pandas_api()
df3_enade = spark.read.csv(enade_data_path + 'microdados2017_arq3.txt', header=True, inferSchema=True, sep=';')
pd_df3_enade = df3_enade.pandas_api()
df5_enade = spark.read.csv(enade_data_path + 'microdados2017_arq5.txt', header=True, inferSchema=True, sep=';')
pd_df5_enade = df5_enade.pandas_api()
df6_enade = spark.read.csv(enade_data_path + 'microdados2017_arq6.txt', header=True, inferSchema=True, sep=';')
pd_df6_enade = df6_enade.pandas_api()
print('SUCCESS - EXTRACTION\n')

# CONSUMPTION --------------------------------------------------------------------------------------------------------------------
# Q1 - Qual era o número de alunos de cursos de Filosofia inscritos no ENADE 2017?
q1 = df1_enade.filter((df1_enade.CO_GRUPO == 3201) | (df1_enade.CO_GRUPO == 3202)).count()
print('\n1 answer =', q1, '\n')
# Q2 - Qual é o número de alunos dos cursos de Filosofia do sexo Masculino?
pd_15 = ps.concat([pd_df1_enade, pd_df5_enade[['TP_SEXO']]], axis=1)
q2 = len(pd_15.loc[((pd_15['CO_GRUPO'] == 3201) | (pd_15['CO_GRUPO'] == 3202)) & (pd_15['TP_SEXO'] == 'M')])
print('\n2 answer =', q2, '\n')
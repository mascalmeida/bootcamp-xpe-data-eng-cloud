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
enem_data_path = module_path + "/data/enem2020/"

# Create spark session
spark = (
    SparkSession.builder.appName("challenge2_module3")
    .getOrCreate()
)

print('SUCCESS - GENERAL SETTINGS\n')

# EXTRACTION --------------------------------------------------------------------------------------------------------------------
## Reading data from raw layer
df_enem = spark.read.csv(enem_data_path + 'MICRODADOS_ENEM_2020.csv', header=True, inferSchema=True, sep=';')
print('SUCCESS - EXTRACTION\n')

# ANSWERS --------------------------------------------------------------------------------------------------------------------
## 1. Quantos alunos não quiseram declarar a cor/raça em 2020 (Entenda a opção “não declarado” nessa pergunta)?
df_enem.filter((df_enem.TP_COR_RACA == 0)).count()
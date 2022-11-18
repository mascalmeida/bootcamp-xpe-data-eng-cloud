# GENERAL SETTINGS --------------------------------------------------------------------------------------------------------------------

# Packages
## Spark packages
import pyspark
from pyspark.sql import SparkSession
## General packages
import os

# Paths
## Main directory
module_path = os.path.abspath(os.path.join('..'))
## cnaes data directory
cnaes_data_path = module_path + "/data/cnaes/"
## estabelecimentos data directory
estab_data_path = module_path + "/data/estabelecimentos/"

# Create spark session
spark = (
    SparkSession.builder.appName("challenge2_module2")
    .getOrCreate()
)

print('SUCCESS - GENERAL SETTINGS\n')

# EXTRACTION --------------------------------------------------------------------------------------------------------------------
## Reading data from raw layer
raw_estab = spark.read.csv(estab_data_path, header=True, inferSchema=True, sep=';')
print('SUCCESS - EXTRACTION\n')

## Transform from many .csv to only one .csv
raw_estab.write.mode("overwrite").csv(estab_data_path + "csv/estabelecimentos.csv")

## Transform from .csv to parquet
raw_estab.write.mode("overwrite").parquet(estab_data_path + "parquet/estabelecimentos.parquet")
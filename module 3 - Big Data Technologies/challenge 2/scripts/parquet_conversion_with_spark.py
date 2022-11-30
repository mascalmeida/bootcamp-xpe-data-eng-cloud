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

# CONVERSION --------------------------------------------------------------------------------------------------------------------
## Reading data from raw layer
raw_enade = spark.read.csv(enade_data_path, header=True, inferSchema=True, sep=';')
## Transform from .txt to parquet
raw_enade.write.mode("overwrite").parquet(staging_data_path + "enade2017.parquet")
print('SUCCESS - CONVERSION\n')
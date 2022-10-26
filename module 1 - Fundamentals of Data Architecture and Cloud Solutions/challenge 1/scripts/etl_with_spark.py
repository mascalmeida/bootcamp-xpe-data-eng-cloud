# General Settings ----------------------------------------------------
# Packages
import pyspark
from pyspark.sql import SparkSession
# Create spark session
spark = (
	SparkSession.builder.appName("ETLEnem2020")
	.getOrCreate()
)

# Extraction ----------------------------------------------------
# Read data from Amazon S3 bucket
enem_raw = (
	spark
	.read
	.format("csv")
	.option("header", True)
	.option("inferSchema", True)
	.option("delimiter", ";")
	.load("s3://datalake-mascalmeida-284935897552/raw-data/")
)

# Transformation ----------------------------------------------------
# Select the main columns
df = (
    enem_raw
    .select('NU_ANO', 'TP_SEXO', 'NU_NOTA_MT', 'NU_NOTA_CH', 'SG_UF_ESC', 'CO_MUNICIPIO_ESC', 'NO_MUNICIPIO_ESC', 'CO_MUNICIPIO_PROVA', 'NO_MUNICIPIO_PROVA', 'Q008', 'Q002')
)

# Loading ----------------------------------------------------
# Saving on consumer-zone
(
    df
    .write
    .mode("overwrite")
    .format("parquet")
    .partitionBy("NU_ANO")
    .save("s3://datalake-mascalmeida-284935897552/consumer-zone/enem2020")
)
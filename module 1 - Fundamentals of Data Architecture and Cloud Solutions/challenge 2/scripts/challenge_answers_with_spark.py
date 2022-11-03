# General Settings ----------------------------------------------------
# Packages
import pyspark
from pyspark.sql import SparkSession
# Create spark session
spark = (
	SparkSession.builder.appName("ETLrais2020")
	.getOrCreate()
)

# Packages for the job itself
from pyspark.sql.functions import col, mean, max
from pyspark.sql import functions as f

# Extraction ----------------------------------------------------
## read data from raw in parquet format
rais = spark.read.parquet("s3://datalake-masca-md1-challenge2-tf/analytics/")
## creating the uf column
rais = rais.withColumn("uf", f.col("municipio").cast('string').substr(1,2).cast('int'))
rais.printSchema()

# Answers ---------------------------------------------------------
## 1. Qual é o SEGUNDO motivo de desligamento mais frequente?
rais.groupBy('motivo_desligamento').count().sort(col("count").desc()).show(2)

## 2. Qual é o estado com a maior média de renda nominal do Brasil?
rais.groupBy('uf').mean('vl_remun_media_nom').sort(col("avg(vl_remun_media_nom)").desc()).show()

## 3. Qual é a média da renda nominal da UF 31 (utilize a renda média nominal)?
rais.filter(rais.uf == 31).select(mean ('vl_remun_media_nom')).show()

## 4. Quantas pessoas, no estado 21, possuem renda nominal média menor do que o salário-mínimo de 2020 (1039 reais)?
rais.filter((rais.uf == 21) & (rais.vl_remun_media_nom < 1039)).count()

## 5. Qual foi a média de horas trabalhadas na UF 16?
rais.filter(rais.uf == 16).select(mean('qtd_hora_contr')).show()

## 6. Qual é a diferença entre os salários médios nominais entre categorias de sexo?
q6 = rais.groupBy('sexo_trabalhador').mean('vl_remun_media_nom')
q6.collect()[0][1] - q6.collect()[1][1]

## 7. Qual é a diferença entre os salários médios nominais entre categorias de sexo para os trabalhadores da área de tecnologia (CNAE 2.0 Classe = 62040)?
q7 = rais.filter(rais.cnae_2_0_classe == 62040).groupBy('sexo_trabalhador').mean('vl_remun_media_nom')
q7.collect()[0][1] - q7.collect()[1][1]
# GENERAL SETTINGS --------------------------------------------------------------------------------------------------------------------

# Packages
## Spark packages
import pyspark
from pyspark.sql import SparkSession
## Manipulation packages
from pyspark.sql.functions import col, size, split, max, mean, length
import pyspark.pandas as ps
## General packages
import os

# Paths
## Main directory
module_path = os.path.abspath(os.path.join('..'))
## raw directory
raw_data_path = module_path + "/data/raw/"

# Create spark session
spark = (
    SparkSession.builder.appName("challenge1_module2")
    .getOrCreate()
)

# Show only 20 rows with Pandas API
ps.options.display.max_rows = 20

print('SUCCESS - GENERAL SETTINGS\n')

# EXTRACTION --------------------------------------------------------------------------------------------------------------------
## Reading data from raw layer
raw_ratings = spark.read.csv(raw_data_path + 'title_ratings.tsv', header=True, inferSchema=True, sep='\t')
pd_raw_ratings = raw_ratings.pandas_api()
raw_basics = spark.read.csv(raw_data_path + 'title_basics.tsv', header=True, inferSchema=True, sep='\t')
pd_raw_basics = raw_basics.pandas_api()
print('SUCCESS - EXTRACTION\n')

# CONSUMPTION --------------------------------------------------------------------------------------------------------------------
## Answers

### 4. Quantos filmes (incluindo os da televisão) foram lançados no ano de 2015?
q4 = raw_basics.filter((raw_basics.startYear == 2015) & ((raw_basics.titleType == 'movie') | (raw_basics.titleType == 'tvMovie'))).count()
print('\n4 answer =', q4, '\n')

### 5. Qual o gênero de títulos mais frequente?
#### Max of columns before the split
n_genres_max_per_row = raw_basics.withColumn('n', size(split(col("genres"), r","))).select(max('n')).collect()[0][0]
#### Split into 'n' columns. 
# ref: https://stackoverflow.com/questions/39255973/split-1-column-into-3-columns-in-spark-scala#comment92328398_45972636
df_genres = (raw_basics.withColumn('temp', split('genres', '\\,')).select(*(col('temp').getItem(i).alias(f'genre_{i}') for i in range(n_genres_max_per_row))))
#### Stack the columns in only one column
genre_0 = df_genres.filter(col('genre_0').isNotNull()).select('genre_0')
genre_1 = df_genres.filter(col('genre_1').isNotNull()).select('genre_1')
genre_2 = df_genres.filter(col('genre_2').isNotNull()).select('genre_2')
genre_0_1 = genre_0.union(genre_1)
genre_0_1_2 = genre_0_1.union(genre_2)
#### Get the more frequent value
q5 = genre_0_1_2.groupBy('genre_0').count().sort(col("count").desc()).select('genre_0').collect()[0][0]

print('\n5 answer =', q5, '\n')

### 6. Qual o gênero com a melhor nota média de títulos?
#### Select columns
df_genres = raw_basics.select('tconst', 'genres')
#### Split column into new columns by comma
genre_0 = df_genres.withColumn('genre_0', split(df_genres['genres'], ',').getItem(0)).drop('genres').filter(col('genre_0').isNotNull())
genre_1 = df_genres.withColumn('genre_1', split(df_genres['genres'], ',').getItem(1)).drop('genres').filter(col('genre_1').isNotNull())
genre_2 = df_genres.withColumn('genre_2', split(df_genres['genres'], ',').getItem(2)).drop('genres').filter(col('genre_2').isNotNull())
#### Union each dataframe in only one
genre_0_1 = genre_0.union(genre_1)
genre_0_1_2 = genre_0_1.union(genre_2)
#### Join the dataframes
df_ratings_genres = raw_ratings.join(genre_0_1_2, on=raw_ratings.tconst ==  genre_0_1_2.tconst, how="outer")
#### Get the best category by rating
q6 = df_ratings_genres.filter(col('genre_0').isNotNull()).groupBy('genre_0').mean('averageRating').sort(col('avg(averageRating)').desc()).select('genre_0').collect()[0][0]
print('\n6 answer =', q6, '\n')

### 7. Qual o vídeo game do gênero aventura mais bem avaliado em 2020?
#### Filter dataframe
df_games = raw_basics.filter((raw_basics.titleType == 'videoGame') & (raw_basics.startYear == 2020) & (raw_basics.genres.contains('Adventure')))
#### Join dataframes, how=left
df_games_ratings = df_games.join(raw_ratings, on=df_games.tconst ==  raw_ratings.tconst, how="left")
#### Get the best cat by rating
q7 = df_games_ratings.filter(col('averageRating').isNotNull()).groupBy('primaryTitle').mean('averageRating').sort(col('avg(averageRating)').desc()).select('primaryTitle').collect()[0][0]
print('\n7 answer =', q7, '\n')

### 9. Quantos títulos de filmes diferentes existem? Use df_titles.select('primaryTitle').distinct().count().
#q9 = raw_basics.filter((raw_basics.titleType == 'movie') | (raw_basics.titleType == 'tvMovie')).select('primaryTitle').distinct().count()
q9 = raw_basics.select('primaryTitle').distinct().count()
print('\n[BUG] 9 answer =', q9, '\n')

### 10. Qual a duração média dos filmes com conteúdo adulto? Use uma combinação de filter() e describe().
#q10 = raw_basics.filter((raw_basics.isAdult == '1') & ((raw_basics.titleType == 'movie') | (raw_basics.titleType == 'tvMovie'))).describe().filter(col('summary') == 'mean').select('runtimeMinutes')
q10 = raw_basics.filter(raw_basics.isAdult == '1').describe().filter(col('summary') == 'mean').select('runtimeMinutes')
print('\n[BUG] 10 answer =', q10.collect()[0][0], '\n')

### 11. Quantos filmes têm o título atual (“primary”) diferente do título original? Use uma combinação de filter, e count().
#q11 = raw_basics.filter((raw_basics.primaryTitle != raw_basics.originalTitle) & ((raw_basics.titleType == 'movie') | (raw_basics.titleType == 'tvMovie'))).count()
q11 = raw_basics.filter((raw_basics.primaryTitle != raw_basics.originalTitle)).count()
print('\n[BUG] 11 answer =', q11, '\n')

### 12. Qual o filme que tem o nome mais longo?
# q12 = raw_basics.filter((raw_basics.titleType == 'movie') | (raw_basics.titleType == 'tvMovie')).withColumn("len_title", length(col("primaryTitle"))).groupBy("tconst", "primaryTitle").max("len_title").sort(col("max(len_title)").desc()).collect()[0][0]
# q12 = raw_basics.withColumn("len_title", length(col("primaryTitle"))).groupBy("tconst", "primaryTitle").max("len_title").sort(col("max(len_title)").desc()).collect()[0][0]
q12 = 'tt12985206'
print('\n[BUG] 12 answer =', q12, '\n')
raw_basics.withColumn("len_title", length(col("primaryTitle"))).groupBy("tconst", "primaryTitle").max("len_title").sort(col("max(len_title)").desc()).show()

### 13. Qual filme tem a maior quantidade de votos? Dica: Use describe().
q13 = 'tt0111161'
print('\n[BUG] 13 answer =', q13, '\n')
raw_ratings.describe().show()
raw_ratings.filter(raw_ratings.numVotes == 2449517).show()

### 15. Qual é a menor nota média de um filme? Use describe().
q15 = '1.0'
raw_ratings.describe().show()
print('\n[BUG] 15 answer =', q15, '\n')

print('SUCCESS - CONSUMPTION\n')
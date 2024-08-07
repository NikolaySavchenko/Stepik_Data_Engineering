from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Создание SparkSession
spark = SparkSession.builder.appName("Analyse CSV").getOrCreate()

# Чтение CSV-файла
df = spark.read.csv("web_server_logs.csv", header=True, inferSchema=True)

# Группируем данные по IP и считаем количество запросов для каждого IP
ip_grooped = df.groupBy("ip").count().withColumnRenamed("count",
                "request_count").orderBy(col("request_count").desc()).limit(10)
print('Top 10 active IP address:')
ip_grooped.show()

# Группируем данные по HTTP методу и считаем количество запросов
method_grooped = df.groupBy("method").count().withColumnRenamed("count",
                "request_count").orderBy(col("request_count").desc())
print('Request count by HTTP method:')
method_grooped.show()

# Считаем количество запросов с ответом 404
no_response = df.filter(col('response_code') == 404)
no_response_count = no_response.count()
print(f'Nomber of 404 respones codes: {no_response_count}')

# Преобразуем столбец timestamp в формат даты
df = df.withColumn("date", to_date(col("timestamp"), "yyyy-MM-dd"))
# Группируем по дате и суммируем количество ответов
date_grooped = df.groupBy("date").sum("response_size").withColumnRenamed("sum(response_size)",
                "total_response_size").orderBy(col("date").desc()).limit(10)
print('Total response size by day:')
date_grooped.show()

spark.stop()
import os
import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, avg, count, desc


os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

spark = SparkSession.builder.appName("praktika").getOrCreate()

df = spark.read.csv("transactions.csv", header=True, inferSchema=True)

filtr = df.filter(col("status") == "SUCCESS")

result = filtr.groupBy("user_id").agg(sum("amount").alias("total_spent"), count("amount").alias("transaction_count")).orderBy(desc("total_spent"))

result.show(10)
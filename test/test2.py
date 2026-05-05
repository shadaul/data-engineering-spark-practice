import os
import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, avg, count


os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

spark = SparkSession.builder.appName("praktika").getOrCreate()

df = spark.read.csv("transactions.csv", header=True, inferSchema=True)

filtr = df.filter(col("status") == "FAILED")

grup = filtr.groupBy("user_id").agg(count("user_id").alias("fail_count"),avg("amount").alias("avg_fail_amount"))

grup.orderBy(col("fail_count").desc()).show()
import os
import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum


os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

spark = SparkSession.builder.appName('praktika').getOrCreate()

df = spark.read.csv('transactions.csv', header=True, inferSchema=True)

filtacia = df.filter(col("status") == 'SUCCESS')

cal = filtacia.groupBy("user_id").agg(sum("amount").alias("total_sum"))

cal.filter(col("total_sum") > 1000).show()
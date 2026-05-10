import os
import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, avg, count, desc, when


os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

spark = SparkSession.builder.appName("prakrika").getOrCreate()

df = spark.read.csv("transactions.csv", header=True, inferSchema=True)

filtr = df.filter(col("status") == "SUCCESS")

grup = filtr.groupBy("user_id").agg(count("amount").alias("total_count"), sum("amount").alias("total_spent"))

result = grup.filter(col("total_count") >= 2) \
             .orderBy(desc("total_spent")) \
             .limit(3)

result.show()
import os
import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, avg, count, desc, when


os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

spark = SparkSession.builder.appName("praktika").getOrCreate()

df = spark.read.csv("transactions.csv", header=True, inferSchema=True)

filtr = df.filter(col("status") == "SUCCESS")

df_categorized = filtr.withColumn(
    "check_size",
    when(col("amount") < 1000, "Small")
    .when((col("amount") >= 1000) & (col("amount") <= 5000), "medium")
    .otherwise("large")
)

result = df_categorized.groupBy("check_size").agg(count("amount"))

result.show(10)
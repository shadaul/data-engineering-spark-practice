import os
import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, avg, count


os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

spark = SparkSession.builder.appName("praktika").getOrCreate()

df = spark.read.csv("transactions.csv", header=True, inferSchema=True)

filtr = df.filter((col("status") == "SUCCESS") & (col("amount") > 5000))
                  
calc = filtr.withColumn("cashback", col("amount") * 0.05)

calc.select("user_id", "amount", "cashback").show(5)
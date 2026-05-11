import os
import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, avg, count, desc


os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

spark = SparkSession.builder.appName('praktika').getOrCreate()

data = [
    {'user_id': 101, 'action': 'buy', 'amount': 150},
    {'user_id': 102, 'action': 'click', 'amount': 0},
    {'user_id': 101, 'action': 'buy', 'amount': 250},
    {'user_id': 103, 'action': 'buy', 'amount': 500},
    {'user_id': 102, 'action': 'buy', 'amount': 50},
    {'user_id': 103, 'action': 'buy', 'amount': 100}
]

df = spark.createDataFrame(data)

filtr = df.filter(col('action') == 'buy')

result = filtr.groupBy('user_id').agg(sum('amount').alias('total_spent')).orderBy(desc('total_spent'))

result.show(2)
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("MyFirstSparkPractice")
    .getOrCreate()
)


data = [
    (101, "ShadowNinja", 500),
    (102, "GamerPro", 150),
    (103, "NoobMaster", 1000)
]

columns = ["player_id", "nickname", "amount_spent"]

df = spark.createDataFrame(data, columns)

df.show()

spark.stop()
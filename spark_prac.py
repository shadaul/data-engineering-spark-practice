import os
import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum

# Системный костыль для Windows (это оставляем как есть)
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

# 1. Инициализация (Создаем начальника)
spark = SparkSession.builder.appName("Practice").getOrCreate()

# ==========================================
# --- ТВОЯ ЗОНА ОТВЕТСТВЕННОСТИ НАЧИНАЕТСЯ ТУТ ---

# ШАГ 1: Прочитай данные из файла "transactions.csv"
# Подсказка: у объекта spark есть метод read.csv(). 
# Внутри скобок нужно передать 3 аргумента: имя файла в кавычках, header=True (чтобы первая строка стала названиями колонок) и inferSchema=True (чтобы цифры стали цифрами, а не текстом).
df = spark.read.csv('transactions.csv', header=True, inferSchema=True)

# ШАГ 2: Узкая трансформация (Фильтрация)
# Оставь только те транзакции, где статус успешен.
# Подсказка: используй df.filter(). Внутри скобок напиши условие col("status") == "SUCCESS".
successful_df = df.filter(col('status') == 'SUCCESS')

# ШАГ 3: Широкая трансформация (Группировка и Агрегация)
# Нам нужно узнать, сколько всего денег потратил каждый клиент (user_id).
# Подсказка: возьми successful_df, примени к нему метод .groupBy("имя_колонки"), а затем сразу метод .agg(sum("колонка_с_деньгами").alias("total_spent"))
agg_df = successful_df.groupBy("user_id").agg(sum("amount").alias("total_spent"))

# ШАГ 4: Action (Действие)
# Заставь Спарк выполнить весь этот план и вывести финальную таблицу на экран.
# Подсказка: примени метод .show() к таблице agg_df.
agg_df.show()

# --- ТВОЯ ЗОНА ОТВЕТСТВЕННОСТИ ЗАКАНЧИВАЕТСЯ ТУТ ---
# ==========================================

# Убиваем сессию, освобождаем память
spark.stop()
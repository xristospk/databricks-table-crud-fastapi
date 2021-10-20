# Databricks notebook source
from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql.window import *
from datetime import datetime

# COMMAND ----------

#Assign variable values
mountPoint = "/mnt/reservoir/databrickscrudapi/"
deltaLakeDb = "crudapidb"
deltaLakeTable = "customer"
deltaPath = mountPoint + deltaLakeDb + "/" + deltaLakeTable + "/"
print(deltaPath)

# COMMAND ----------

dropstatement = "DROP TABLE IF EXISTS " + deltaLakeDb + "." + deltaLakeTable
spark.sql(dropstatement)
dbutils.fs.rm(deltaPath, recurse=True)

# COMMAND ----------

spark.sql(f"CREATE DATABASE IF NOT EXISTS {deltaLakeDb}")

createTblCmd = f"""
CREATE TABLE IF NOT EXISTS {deltaLakeDb}.{deltaLakeTable}
(
   Id           INT
  ,Name	        STRING            
  ,Email        STRING           
  ,Country      STRING
  ,Car          STRING
  ,FavoriteFood STRING
  ,Registered   DATE
  ,Active       BOOLEAN
  ,Age          INTEGER
)
USING DELTA
LOCATION "{deltaPath}"
"""

spark.sql(createTblCmd)

# COMMAND ----------

rawdata = mountPoint + "crudapidata.csv"
df = spark.read.option("delimiter", ";").option("header", True).option("inferSchema", True).csv(rawdata)
df = df.withColumn("Registered", to_date(col('Registered'), "MM/dd/yyyy"))
df = df.withColumn("Id", row_number().over(Window.orderBy("Name", "Email")))

tabeleSchema = spark.read.table(deltaLakeDb + "." + deltaLakeTable)
df.select(tabeleSchema.columns).write.insertInto("{}.{}".format(deltaLakeDb, deltaLakeTable), overwrite=True)

# COMMAND ----------

# MAGIC %sql 
# MAGIC select * from crudapidb.customer

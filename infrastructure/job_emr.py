
from pyspark.sql.functions import mean, max, col, count
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder.appName("ExerciseSpark")
    .getOrCreate()
)


enem = (spark
.read
.format("csv")
.option("header", True)
.option("inferschema", True)
.option("delimiter", ";")
.load("s3://datalake-educosta-igti-edc/raw-data/enem/")
)


(
enem
.write
.mode("overwrite")
.format("parquet")
.partitionBy("year")
.save("s3://datalake-educosta-igti-edc/staging/enem")
)
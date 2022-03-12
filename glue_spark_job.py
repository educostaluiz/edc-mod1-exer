import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: ['JOB_NAME']
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)


# a partir daqui, exatamente o mesmo jcodigo do EMR
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
.save("s3://datalake-educosta-igti-edc/staging/enem_glue")
)


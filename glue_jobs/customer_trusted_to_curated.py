import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality
from awsglue import DynamicFrame

def sparkSqlQuery(glueContext, query, mapping, transformation_ctx) -> DynamicFrame:
    for alias, frame in mapping.items():
        frame.toDF().createOrReplaceTempView(alias)
    result = spark.sql(query)
    return DynamicFrame.fromDF(result, glueContext, transformation_ctx)
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Default ruleset used by all target nodes with data quality enabled
DEFAULT_DATA_QUALITY_RULESET = """
    Rules = [
        ColumnCount > 0
    ]
"""

# Script generated for node Customer_landing
Customer_landing_node1779689045072 = glueContext.create_dynamic_frame.from_catalog(database="stedi", table_name="customer_landing", transformation_ctx="Customer_landing_node1779689045072")

# Script generated for node accelerometer_landing
accelerometer_landing_node1779689110525 = glueContext.create_dynamic_frame.from_catalog(database="stedi", table_name="accelerometer_landing", transformation_ctx="accelerometer_landing_node1779689110525")

# Script generated for node SQL Query
SqlQuery0 = '''
SELECT DISTINCT
    c.serialnumber,
    c.sharewithpublicasofdate,
    c.birthday,
    c.registrationdate,
    c.sharewithresearchasofdate,
    c.customername,
    c.email,
    c.lastupdatedate,
    c.phone,
    c.sharewithfriendsasofdate
FROM c
WHERE c.sharewithresearchasofdate IS NOT NULL
AND EXISTS (
SELECT 1
FROM a 
WHERE lower(trim(c.email))= lower(trim(a.user))
)
'''
SQLQuery_node1779689328550 = sparkSqlQuery(glueContext, query = SqlQuery0, mapping = {"c":Customer_landing_node1779689045072, "a":accelerometer_landing_node1779689110525}, transformation_ctx = "SQLQuery_node1779689328550")

# Script generated for node Amazon S3
EvaluateDataQuality().process_rows(frame=SQLQuery_node1779689328550, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1779689008334", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
AmazonS3_node1779689615438 = glueContext.getSink(path="s3://arshad-stedi-project/customer_curated/", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=[], compression="snappy", enableUpdateCatalog=True, transformation_ctx="AmazonS3_node1779689615438")
AmazonS3_node1779689615438.setCatalogInfo(catalogDatabase="stedi",catalogTableName="customer_curated")
AmazonS3_node1779689615438.setFormat("json")
AmazonS3_node1779689615438.writeFrame(SQLQuery_node1779689328550)
job.commit()
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

# Script generated for node AWS Glue Data Catalog accelerator
AWSGlueDataCatalogaccelerator_node1779699286042 = glueContext.create_dynamic_frame.from_catalog(database="stedi", table_name="accelerometer_landing", transformation_ctx="AWSGlueDataCatalogaccelerator_node1779699286042")

# Script generated for node customer landing
customerlanding_node1779699330442 = glueContext.create_dynamic_frame.from_catalog(database="stedi", table_name="customer_landing", transformation_ctx="customerlanding_node1779699330442")

# Script generated for node SQL Query
SqlQuery0 = '''
SELECT
    a.user,
    a.timestamp,
    a.x,
    a.y,
    a.z
FROM a
WHERE EXISTS (
    SELECT 1
    FROM c
    WHERE lower(trim(a.user)) = lower(trim(c.email))
    AND c.sharewithresearchasofdate IS NOT NULL
)
'''
SQLQuery_node1779688563229 = sparkSqlQuery(glueContext, query = SqlQuery0, mapping = {"a":AWSGlueDataCatalogaccelerator_node1779699286042, "c":customerlanding_node1779699330442}, transformation_ctx = "SQLQuery_node1779688563229")

# Script generated for node Amazon S3
EvaluateDataQuality().process_rows(frame=SQLQuery_node1779688563229, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1779688129002", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
AmazonS3_node1779688753638 = glueContext.getSink(path="s3://arshad-stedi-project/accelerometer_trusted/", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=[], enableUpdateCatalog=True, transformation_ctx="AmazonS3_node1779688753638")
AmazonS3_node1779688753638.setCatalogInfo(catalogDatabase="stedi",catalogTableName="accelerometer_trusted")
AmazonS3_node1779688753638.setFormat("glueparquet", compression="snappy")
AmazonS3_node1779688753638.writeFrame(SQLQuery_node1779688563229)
job.commit()
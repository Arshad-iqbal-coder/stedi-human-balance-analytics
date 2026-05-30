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

# Script generated for node step_trainer_landing
step_trainer_landing_node1779701518744 = glueContext.create_dynamic_frame.from_catalog(database="stedi", table_name="step_trainer_landing", transformation_ctx="step_trainer_landing_node1779701518744")

# Script generated for node customer_curated
customer_curated_node1779701678453 = glueContext.create_dynamic_frame.from_catalog(database="stedi", table_name="customer_curated", transformation_ctx="customer_curated_node1779701678453")

# Script generated for node SQL Query
SqlQuery0 = '''
SELECT
    s.sensorreadingtime,
    s.serialnumber,
    s.distancefromobject
FROM s
INNER JOIN c
ON lower(trim(s.serialnumber)) = lower(trim(c.serialnumber))
'''
SQLQuery_node1779701740057 = sparkSqlQuery(glueContext, query = SqlQuery0, mapping = {"s":step_trainer_landing_node1779701518744, "c":customer_curated_node1779701678453}, transformation_ctx = "SQLQuery_node1779701740057")

# Script generated for node Amazon S3
EvaluateDataQuality().process_rows(frame=SQLQuery_node1779701740057, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1779701088386", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
AmazonS3_node1779702118810 = glueContext.getSink(path="s3://arshad-stedi-project/step_trainer_trusted/", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=[], enableUpdateCatalog=True, transformation_ctx="AmazonS3_node1779702118810")
AmazonS3_node1779702118810.setCatalogInfo(catalogDatabase="stedi",catalogTableName="step_trusted")
AmazonS3_node1779702118810.setFormat("glueparquet", compression="snappy")
AmazonS3_node1779702118810.writeFrame(SQLQuery_node1779701740057)
job.commit()
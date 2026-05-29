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
Customer_landing_node1779702650372 = glueContext.create_dynamic_frame.from_catalog(database="stedi", table_name="customer_landing", transformation_ctx="Customer_landing_node1779702650372")

# Script generated for node step_trainer_landing
step_trainer_landing_node1779702483689 = glueContext.create_dynamic_frame.from_catalog(database="stedi", table_name="step_trainer_landing", transformation_ctx="step_trainer_landing_node1779702483689")

# Script generated for node accelerometer_landing
accelerometer_landing_node1779702622059 = glueContext.create_dynamic_frame.from_catalog(database="stedi", table_name="accelerometer_landing", transformation_ctx="accelerometer_landing_node1779702622059")

# Script generated for node SQL Query
SqlQuery0 = '''
SELECT 
    a.user,
    a.timestamp,
    a.x,
    a.y,
    a.z,
    s.sensorreadingtime,
    s.serialnumber,
    s.distancefromobject
FROM a 
INNER JOIN s 
ON a.timestamp =s.sensorreadingtime 

INNER JOIN c 

ON (lower(trim(c.email))= lower(trim(a.user))
AND 
lower(trim(s.serialnumber))=lower(trim(c.serialnumber)))

where   c.sharewithresearchasofdate IS NOT NULL
'''
SQLQuery_node1779702682826 = sparkSqlQuery(glueContext, query = SqlQuery0, mapping = {"c":Customer_landing_node1779702650372, "s":step_trainer_landing_node1779702483689, "a":accelerometer_landing_node1779702622059}, transformation_ctx = "SQLQuery_node1779702682826")

# Script generated for node Amazon S3
EvaluateDataQuality().process_rows(frame=SQLQuery_node1779702682826, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1779702479558", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
AmazonS3_node1779702708598 = glueContext.getSink(path="s3://arshad-stedi-project/machine_learning_curated/", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=[], compression="snappy", enableUpdateCatalog=True, transformation_ctx="AmazonS3_node1779702708598")
AmazonS3_node1779702708598.setCatalogInfo(catalogDatabase="stedi",catalogTableName="machine_learning_curated")
AmazonS3_node1779702708598.setFormat("json")
AmazonS3_node1779702708598.writeFrame(SQLQuery_node1779702682826)
job.commit()
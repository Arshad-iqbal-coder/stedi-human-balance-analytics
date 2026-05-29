CREATE EXTERNAL TABLE IF NOT exists
step_trainer_landing( sensorreadingtime bigint, serialnumber string, distancefromobject int )
ROW FORMAT serde
'org.openx.data.jsonserde.JsonSerDe'
location
's3://arshad-stedi-project/step_trainer_landing/'
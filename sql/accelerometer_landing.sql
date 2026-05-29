CREATE EXTERNAL TABLE IF NOT exists
accelerometer_landing( user string, timestamp bigint, x double, y double, z double )
ROW FORMAT serde
'org.openx.data.jsonserde.JsonSerDe'
location
's3://arshad-stedi-project/accelerometer_landing/'
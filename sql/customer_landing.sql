CREATE EXTERNAL TABLE IF NOT exists
customer_landing( serialnumber string, sharewithpublicasofdate string, birthday string, registrationdate bigint, sharewithresearchasofdate string, customername string, email string, lastupdatedate bigint, phone string, sharewithfriendsasofdate string )
ROW FORMAT serde
'org.openx.data.jsonserde.JsonSerDe'
location
's3://arshad-stedi-project/customer_landing/'
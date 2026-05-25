SELECT 
    
    s.sensorreadingtime,
    s.serialnumber,
    s.distancefromobject
FROM s
WHERE EXISTS (
SELECT 1
FROM c 
WHERE lower(trim(s.serialnumber))=lower(trim(c.serialnumber))
AND  c.sharewithresearchasofdate IS NOT NULL

AND EXISTS (
SELECT 1
FROM a 
WHERE lower(trim(c.email))= lower(trim(a.user))
))
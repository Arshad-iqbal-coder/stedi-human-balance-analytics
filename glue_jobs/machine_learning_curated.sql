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
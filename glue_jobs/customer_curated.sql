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
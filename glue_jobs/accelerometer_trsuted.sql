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
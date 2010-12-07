
CREATE TABLE q7 (id SERIAL primary key,  n1 char(50),n2 char(50), c int);

INSERT INTO q7(n1,n2, c)
SELECT f2.name AS field2, f1.name AS field1, count(f1.name) AS shared 
FROM grants, grant_fields gf1, fields f1, grant_fields gf2, fields f2 
WHERE grants.id=gf1.grantid AND gf1.fieldid=f1.id 
AND grants.id=gf2.grantid AND gf2.fieldid=f2.id 
AND f1.id < f2.id 
GROUP BY field2, field1
ORDER BY shared DESC
LIMIT 5;

select * from q7;
select count(*) from pg_prov;

DROP table q7;

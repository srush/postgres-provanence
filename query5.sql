CREATE TABLE q5 (id SERIAL primary key,  n char(50), numdir int);

INSERT INTO q5(n, numdir)
SELECT researchers.name, count(DISTINCT(directorate)) AS numdir 
FROM grants, grant_researchers, researchers, grant_programs, programs 
WHERE grants.id=grant_researchers.grantid AND grant_researchers.researcherid=researchers.id
AND grants.id=grant_programs.grantid AND grant_programs.programid=programs.id 
GROUP BY researchers.name
HAVING count(distinct(directorate))>=6
ORDER BY numdir DESC
LIMIT 10;

select * from q5;
select count(*) from pg_prov;
DROP table q5;


CREATE TABLE q8_1 (a SERIAL primary key, id int, yr int);

INSERT INTO q8_1 (id, yr)
SELECT researchers.id, extract('year' from started) AS yr 
FROM grants, grant_researchers, researchers, orgs 
WHERE grants.id=grant_researchers.grantid 
AND grant_researchers.researcherid=researchers.id 
AND researchers.org=orgs.id 
AND orgs.name LIKE '%Massachusetts Institute of Technology%'
GROUP BY researchers.id, yr 
HAVING SUM(amount)>1000000;

CREATE TABLE q8_2 (a SERIAL primary key, id int , year1 int, year3 int);

INSERT INTO q8_2 (id, year1, year3)
SELECT t1.id, t1.yr AS year1, t3.yr AS year3 
FROM q8_1 t1, q8_1 t3 
WHERE t1.id=t3.id AND t3.yr=t1.yr+2;


CREATE TABLE q8_3 (id SERIAL primary key, rname char(50));

INSERT INTO q8_3(rname)
SELECT DISTINCT r_out.name
FROM researchers r_out, q8_2 
WHERE r_out.id=q8_2.id 
AND year1+1 NOT IN 
(SELECT extract('year' FROM started) 
FROM grants, researchers r_in, grant_researchers
WHERE grants.id=grant_researchers.grantid 
AND grant_researchers.researcherid=r_in.id
AND r_in.id=r_out.id);

select * from q8_3;

select * from pg_prov;

/*drop table q8_1;
drop table q8_2;
drop table q8_3;*/
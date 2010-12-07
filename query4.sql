CREATE TABLE tempq4 (oid SERIAL primary key,  id int, yr int , numgrants int);
CREATE TABLE q4 (id SERIAL primary key, rname char(100) , numg int, yr int, yr2 int, yr3 int);

INSERT INTO tempq4 (id, yr, numgrants )
SELECT orgs.id, extract('year' from started) AS yr, count(orgs.id) AS numgrants
FROM grants, orgs
WHERE grants.org=orgs.id 
GROUP BY orgs.id, yr 
HAVING count(orgs.id)>=10;

select count(*) from pg_prov;
select count(*) from tempq4;


INSERT INTO q4 (rname, numg, yr,yr2, yr3)
SELECT orgs.name, t1.numgrants, t1.yr AS year1, t2.yr AS year2, t3.yr AS year3 
FROM orgs, tempq4 t1, tempq4 t2, tempq4 t3 
WHERE t1.id=t2.id AND t2.id=t3.id AND orgs.id=t1.id 
AND t1.numgrants=t2.numgrants AND t2.numgrants=t3.numgrants
AND t2.yr=t1.yr+1 AND t3.yr=t2.yr+1;


select count(*) from q4;
select count(*) from pg_prov;

DROP table tempq4;
DROP table q4;

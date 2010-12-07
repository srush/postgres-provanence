CREATE TABLE q6 (id SERIAL primary key,  n char(50), oname char(50), numdir int);

INSERT INTO q6(n, oname, numdir)
SELECT managers.name, orgs.name, SUM(amount) AS total
FROM grants, managers, orgs
WHERE grants.manager=managers.id 
AND grants.org=orgs.id 
GROUP BY managers.name, orgs.name
/*ORDER BY total DESC*/
LIMIT 5;

DROP TABLE q6;
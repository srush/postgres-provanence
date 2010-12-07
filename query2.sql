create table p2 (id SERIAL primary key, rname char(100));

insert into p2 (rname)
SELECT researchers.name
FROM grants, researchers, grant_researchers, orgs  
WHERE started>'1-1-2008' 
AND amount>1000000 AND grants.org=orgs.id 
AND orgs.name like '%Massachusetts Institute of Technology%' 
AND grants.id=grant_researchers.grantid 
AND grant_researchers.researcherid=researchers.id;


select * from p2;
select * from pg_prov;

drop table p2;

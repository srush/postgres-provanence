create table p1 (id SERIAL primary key, title char(100), amount float, r_name char(100));

insert into p1 (title, amount, r_name)
SELECT title, amount, researchers.name 
FROM grants, researchers 
WHERE grants.pi=researchers.id 
AND researchers.name like '%Stonebraker';

select * from p1;
select * from pg_prov;

/*drop table p1;*/

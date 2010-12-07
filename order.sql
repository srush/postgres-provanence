create table dest (id int primary key, val int, val2 int);
create table origin (id int primary key, val int, val2 int);

insert into origin values (10, 5 ,1);
insert into origin values (11, 10,1);
insert into origin values (12, 13,2);

insert into origin values (13, 20, 2);

/*insert into dest select id from origin where name_ig='start';  */
insert into dest select val, val2, count(*) from origin group by val, val2;

/* order by val */

select * from pg_prov;
select * from dest;
delete from pg_prov;
drop table origin;
drop table dest;
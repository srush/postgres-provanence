create table dest (id int primary key, val int);
create table origin (id int primary key, val int);

insert into origin values (10, 5);
insert into origin values (11, 10);
insert into origin values (12, 20);

/*insert into dest select id from origin where name_ig='start';  */
insert into dest select 10, sum(origin.val) from origin;
select * from pg_prov;
select * from dest;
delete from pg_prov;
drop table origin;
drop table dest;
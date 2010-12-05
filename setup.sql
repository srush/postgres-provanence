create table dest (id int , id2 int , name1 char (10), name2 char(10), primary key (id, id2));
create table origin (id int , id2 int , name_ig char(5), primary key (id, id2));
create table origin2 (id int primary key, name_ig char(5));
insert into origin values (10, 100, 'start');
insert into origin values (11, 100, 'hello');
insert into origin2 values (11, 'bye');
/*insert into dest select id from origin where name_ig='start';  */
insert into dest select origin.id, origin2.id + 10, origin.name_ig, origin2.name_ig from origin, origin2 where origin.id = origin2.id;  
select * from pg_prov;
select * from dest;
delete from pg_prov;
drop table origin;
drop table origin2;
drop table dest;
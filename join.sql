create table dest (id int primary key  , val int);
create table origin (id int primary key, val int, a char(500));
create table origin2 (id int primary key, val int,  a char(500));

insert into origin values (10, 100, 'a');
insert into origin values (11, 150 , 'b');
insert into origin values (12, 1123, 'a');
insert into origin values (15, 1123, 'a');
insert into origin2 values (11, 150, 'a');
/*insert into dest select id from origin where name_ig='start';  */

         EXPLAIN       select origin.id, origin.val, origin2.val from origin, origin2 where origin.val = origin2.val;   

insert into dest 
       select origin.id, origin2.val from origin, origin2 where origin.a = origin2.a;
        
select * from pg_prov;
select * from dest;
delete from pg_prov;
drop table origin;
drop table origin2;
drop table dest;
create database cdac;

use cdac;

create table test(
name varchar(25),
age int,
address varchar(40));

select * from test;

insert into test values( 'vansh',20, 'qweryt');


describe test;


drop database cdac;

rename table test to test1;

describe test1;

alter table test1 add tear int;


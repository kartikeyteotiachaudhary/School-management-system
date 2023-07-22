create database kartikey;


use kartikey;


create table student1(sname varchar(30) not null,


dmno int(11) not null primary key,


dob date,


class char(3) not null,


city varchar(20) not null
);



create table emp1(empno int(11) Not Null Primary Key,

ename varchar(20) Not Null,

job varchar(20) Not Null,

hiredate date
);



create table exam1(sname varchar(20) Not Null,

admno int(11) Not Null Primary Key,

per decimal(4,2) Not Null,

result varchar(10) Not Null
);



create table fee1(admno int(11) Not Null Primary Key,

fee varchar(11) Not Null,

month varchar(15) Not Null
);


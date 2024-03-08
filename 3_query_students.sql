select count(*) from students;
select count(*) from students where gender = 'Female';
select count(*) from students where gender = 'Male';
select max(address) from students;

select * from students;
select distinct(id) from students;
select * from students where gender='Male';
select * from students where gender='Female';
select name, address from students where gender = 'Male';
select name, address from students limit 10;
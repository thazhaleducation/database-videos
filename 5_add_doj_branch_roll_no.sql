-- Add uniqueness to rollno
-- 2024CSE001
-- YYYYBRANCHid
alter table students
  add column rollno varchar(15) unique,
  add column doj date,
  add column branch varchar(10);






























-- Describe and default is NULL
describe students;
  
-- populate branch
update students set branch='CSE' where id <= 200;
update students set branch='ECE' where id > 200 AND id <= 400;
update students set branch='EEE' where id > 400 AND id <= 600;
update students set branch='CIVIL' where id > 600 AND id <= 800;
update students set branch='MECH' where id > 800 AND id <= 1003;



















update students set branch='ECE' where id <= 400;
update students set branch='EEE' where id <= 600;
update students set branch='CIVIL' where id <= 800;
update students set branch='MECH' where id <= 1000;


















-- Do it in reverse order
update students set branch='MECH' where id <= 1000;
update students set branch='CIVIL' where id <= 800;
update students set branch='EEE' where id <= 600;
update students set branch='ECE' where id <= 400;
update students set branch='CSE' where id <= 200;

















-- Use NULL
update students set branch=NULL;
update students set branch='CSE' where id <= 200;
update students set branch='ECE' where id <= 400 and branch is NULL;
update students set branch='EEE' where id <= 600 and branch is NULL;
update students set branch='CIVIL' where id <= 800 and branch is NULL;
update students set branch='MECH' where id <= 1000 and branch is NULL;

















-- Select id group by branch
select branch, count(id), min(id), max(id) from students group by branch;




















-- populate doj
update students set doj = NOW();

-- Populate data for rollno (YYYY BRANCHCODE id)
update students set rollno = CONCAT(YEAR(doj),branch,id);

concat(1,2,3)
YEAR(date)
alter table students modify rollno varchar(15);


























update students set rollno = CONCAT(YEAR(doj),branch,lpad(id, 4, '0'));


alter table students modify column doj  date not null default (curdate());


insert into students (name, address, gender, mobile) values ('Trudi Martonfi', 'Suite 77', 'Female', '961 838 7199');
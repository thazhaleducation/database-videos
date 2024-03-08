-- Get rows that are having duplicate id
select id, count(id) from students group by id having count(id) > 1;

-- Delete rows that are duplicate
delete from students where id = 1;

-- Insert again the same row
insert into students (id, name, address, gender, mobile) values (1, 'Trudi Martonfi', 'Suite 77', 'Female', '961 838 7199');

-- Check now for duplicates
select id, count(id) from students group by id having count(id) > 1;

-- Enforcing uniqueness to prevent duplicate id
-- can we have primary key with more than one column?
ALTER TABLE students
ADD CONSTRAINT PK_students PRIMARY KEY (id); 

-- Try adding duplicate row
insert into students (id, name, address, gender, mobile) values (1, 'Trudi Martonfi', 'Suite 77', 'Female', '961 838 7199');

-- Get max id
select max(id) + 1 from students;

-- Add with new id
insert into students (id, name, address, gender, mobile) values (t.id, 'Trudi Martonfi', 'Suite 77', 'Female', '961 838 7199');

-- Un-Enforcing primary KEY
ALTER TABLE students DROP PRIMARY KEY; 

-- Autoincrement & primary key
-- can it be done on varchar?
ALTER TABLE students MODIFY id INT AUTO_INCREMENT PRIMARY KEY;

-- insert without id column
insert into students (name, address, gender, mobile) values ('Trudi Martonfi', 'Suite 77', 'Female', '961 838 7199');

-- Last insert id
select last_insert_id()

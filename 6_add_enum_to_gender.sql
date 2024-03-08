-- Idenfity list of genders
select distinct(gender) from students;

-- Genderwise count
select gender, count(gender) from students group by gender;

-- Options to optimize gender column
-- Repetition. what is master data?
update students set column gender='M' where gender = 'Male';
update students set column gender='F' where gender = 'Female';


update students set column gender='O' where gender <> 'Male' AND gender <> 'Female';
update students set column gender='O' where gender NOT IN ('Male', 'Female');
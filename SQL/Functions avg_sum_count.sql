REM   Script: Functions and whildcard
REM   Ok

select count(*) from hr.employees  
where salary = 24000;

select count(*) from hr.employees  
where salary = 24000 
select avg (salary) from hr.employees  
where JOB_ID IN('IT_prog','FI_ACCOUNT');

select count(*) from hr.employees  
where salary = 24000 
select avg (salary) from hr.employees  
where JOB_ID IN('IT_prog','FI_ACCOUNT');

select count(*) from hr.employees  
where salary = 24000 
select avg (salary) from hr.employees  
where JOB_ID='IT_PROG';

select count(*) from hr.employees  
where salary = 24000 
select avg(SALARY) from hr.employees  
where JOB_ID='IT_PROG';

select count(*) from hr.employees  
where salary = 24000;

select count(*) from hr.employees  
where salary = 24000;

select AVG(SALARY) from HR.EMPLOYEES 
WHERE JOB_ID='IT_PROG';

select count(*) from hr.employees  
where salary = 24000;

select AVG(SALARY) from HR.EMPLOYEES 
WHERE JOB_ID IN('IT_PROG','FI_ACCOUNT');

select count(*) from hr.employees  
where salary = 24000;

select AVG(SALARY) from HR.EMPLOYEES 
WHERE JOB_ID IN('IT_PROG','FI_ACCOUNT');

select job_id from hr.employees 
where job_id like'IT____G';

select count(*) from hr.employees  
where salary = 24000;

select AVG(SALARY) from HR.EMPLOYEES 
WHERE JOB_ID IN('IT_PROG','FI_ACCOUNT');

select job_id, salary from hr.employees 
where job_id like'IT____G';


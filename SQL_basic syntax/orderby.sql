REM   Script: select and order from hr employees
REM   mno

select*from SH.Sales;

select CUST_ID from SH.Sales;

select CUST_ID from SH.Sales;

select *from SH.Sales;

select CUST_ID, AMOUNT_ID from SH.Sales;

select CUST_ID AND AMOUNT_ID from SH.Sales;

select AMOUNT_ID from SH.Sales;

select * from SH.Sales;

select * AMOUNT_SOLD, CUST_ID from SH.Sales;

select * AMOUNT_SOLD from SH.Sales;

select  AMOUNT_SOLD, CUST_ID from SH.Sales;

select  AMOUNT_SOLD, CUST_ID from SH.Sales 
select top n * from SH.Sales ;

select  AMOUNT_SOLD, CUST_ID from SH.Sales 
select TOP N * from SH.Sales ;

select  AMOUNT_SOLD, CUST_ID from SH.Sales 
;

select  AMOUNT_SOLD, CUST_ID from SH.Sales 
;

select  AMOUNT_SOLD, CUST_ID from SH.Sales 
SELECT TOP AMOUNT_SOLD * FROM SH.Sales;

SELECT TOP AMOUNT_SOLD * FROM SH.Sales;

select  AMOUNT_SOLD, CUST_ID from SH.Sales 
;

select  AMOUNT_SOLD, CUST_ID from SH.Sales 
ORDER AMOUNT_SOLD DESC;

SELECT * FROM hr.employees;

SELECT * FROM hr.employees 
select top N* from employees order by salary desc;

SELECT * FROM hr.employees 
select top N* from employees ;

SELECT * FROM hr.employees 
select top N* from employees  
order by salary desc;

SELECT * FROM hr.employees 
select emp_name AS UPPER;

SELECT * FROM hr.employees 
SELECT DISTINCT column1;

SELECT * FROM hr.employees 
SELECT DISTINCT departments, employees;

SELECT DISTINCT departments, employees, ... 
FROM hr.Employees;

select * from hr.employees 
;

select DISTINCT FIRST_NAME, SALARY 
from hr.employees 
 
;

select DISTINCT FIRST_NAME, SALARY 
from hr.employees 
 
SELECT Last_Name from hr.employees 
;

select * from hr.employee 
 
 
;

select* from hr.employee 
;

select * from hr.employees 
;

select * from hr.employees 
select DISTINCT FIRST_NAME, SALARY 
from hr.employees 
select HIRE_DATE FROM hr.employees 
;

select HIRE_DATE FROM hr.employees 
;

select HIRE_DATE FROM hr.employees 
;

SELECT Count(*) AS DistinctDEPARTMENT_NAME 
FROM (SELECT DISTINCT LOCATION_ID FROM HR.DEPARTMENTS);

SELECT * FROM HR.EMPLOYEES;

UPDATE EMPLOYEES SET SALARY=SALARY+(SALARY*5.0/100);

SELECT * FROM HR.EMPLOYEES;

SELECT FIRST_NAME FROM HR.EMPLOYEES WHERE FIRST_NAME LIKE 'A%';

SELECT *FROM HR.EMPLOYEES ;

SELECT COUNT(*) FROM HR.EMPLOYEES WHERE SALARY < 17000;

SELECT * FROM HR.EMPLOYEES WHERE SALARY < 17000;

SELECT * FROM HR.EMPLOYEES WHERE SALARY < 17000;

select count(*) from hr.employees where JOB_ID ='IT_PROG';

select count(*) from hr.employees where JOB_ID ='IT_PROG';

select * from hr.employees where JOB_ID ='IT_PROG';

select * from hr.employees where JOB_ID ='IT_PROG' where salary <17000;

select * from hr.employees where JOB_ID ='IT_PROG', where salary <17000;

select * from hr.employees where JOB_ID ='IT_PROG' and  where salary <17000;

select * from hr.employees where JOB_ID ='IT_PROG';

select * from hr.employees where JOB_ID ='IT_PROG';

select * from hr.employees where JOB_ID ='IT_PROG';

select * from hr.employees where manager_id > 100;

select * from hr.employees where JOB_ID ='IT_PROG';

select * from hr.employees where manager_id > 100;

select count(*) from hr.employees where job_id='FI_ACCOUNT';

select * from hr.employees where JOB_ID ='IT_PROG';

select * from hr.employees where manager_id > 100;

select count(*) from hr.employees where job_id='FI_ACCOUNT';

update hr.employees set salary=salay+(salary*5/100);

select * from hr.employees where JOB_ID ='IT_PROG';

select * from hr.employees where manager_id > 100;

select count(*) from hr.employees where job_id='FI_ACCOUNT';

update hr.employees set SALARY=SALARY+(SALARY*5.0/100.0);

select * from hr.employees where JOB_ID ='IT_PROG';

select * from hr.employees where manager_id > 100;

select count(*) from hr.employees where job_id='FI_ACCOUNT';

select * from hr.employees where FIRST_NAME like '______A';

select * from hr.employees where JOB_ID ='IT_PROG';

select * from hr.employees where manager_id > 100;

select count(*) from hr.employees where job_id='FI_ACCOUNT';

select * from hr.employees where FIRST_NAME like '____A';

select * from hr.employees where JOB_ID ='IT_PROG';

select * from hr.employees where manager_id > 100;

select count(*) from hr.employees where job_id='FI_ACCOUNT';

select * from hr.employees where FIRST_NAME like 'A';

select * from hr.employees where JOB_ID ='IT_PROG';

select * from hr.employees where manager_id > 100;

select count(*) from hr.employees where job_id='FI_ACCOUNT';

select * from hr.employees where FIRST_NAME  like '   A';

select * from hr.employees where JOB_ID ='IT_PROG';

select * from hr.employees where JOB_ID ='IT_PROG';

select * from hr.employees where manager_id > 100;

select * from hr.employees where manager_id > 100;

select count(*) from hr.employees where job_id='FI_ACCOUNT';

select count(*) from hr.employees where job_id='FI_ACCOUNT';

select * from hr.employees where FIRST_NAME  like '   A';

select * from hr.employees where FIRST_NAME  like '   A';

select * from hr.employees wheren salary between 9000 and 17000;

select * from hr.employees wheren salary between 9000 and 17000;

select * from hr.employees where JOB_ID ='IT_PROG';

select * from hr.employees where manager_id > 100;

select count(*) from hr.employees where job_id='FI_ACCOUNT';

select * from hr.employees where FIRST_NAME  like '   A';

select * from hr.employees wheren salary between 9000 and 17000;

select * from hr.employees where JOB_ID ='IT_PROG';

select * from hr.employees where manager_id > 100;

select count(*) from hr.employees where job_id='FI_ACCOUNT';

select * from hr.employees where FIRST_NAME  like '   A';

select * from hr.employees where salary between 9000 and 17000;

select * from hr.employees where JOB_ID ='IT_PROG';

select * from hr.employees where manager_id > 100;

select count(*) from hr.employees where job_id='FI_ACCOUNT';

select * from hr.employees where FIRST_NAME  like '   A';

select * from hr.employees where salary between 9000 and 10000;

select * from hr.employees where JOB_ID ='IT_PROG';

select * from hr.employees where manager_id > 100;

select count(*) from hr.employees where job_id='FI_ACCOUNT';

select * from hr.employees where FIRST_NAME  like '   A';

select * from hr.employees where salary between 9000 and 10000;

select FIRST_NAME group by JOB_ID;

select * from hr.employees where JOB_ID ='IT_PROG';

select * from hr.employees where manager_id > 100;

select count(*) from hr.employees where job_id='FI_ACCOUNT';

select * from hr.employees where FIRST_NAME  like '   A';

select * from hr.employees where salary between 9000 and 10000;

select FIRST_NAME from hr.employees  
group by JOB_ID;

select * from hr.employees where JOB_ID ='IT_PROG';

select * from hr.employees where manager_id > 100;

select count(*) from hr.employees where job_id='FI_ACCOUNT';

select * from hr.employees where FIRST_NAME  like '   A';

select * from hr.employees where salary between 9000 and 10000;

select * from hr.employees  
group by JOB_ID;

select * from hr.employees where JOB_ID ='IT_PROG';

select * from hr.employees where manager_id > 100;

select count(*) from hr.employees where job_id='FI_ACCOUNT';

select * from hr.employees where FIRST_NAME  like '   A';

select * from hr.employees where salary between 9000 and 10000;

select * from hr.employees  
order by JOB_ID;

select * from hr.employees where JOB_ID ='IT_PROG';

select * from hr.employees where manager_id > 100;

select count(*) from hr.employees where job_id='FI_ACCOUNT';

select * from hr.employees where FIRST_NAME  like '   A';

select * from hr.employees where salary between 9000 and 10000;

select FIRST_NAME from hr.employees  
order by JOB_ID;

select * from hr.employees where JOB_ID ='IT_PROG';

select * from hr.employees where manager_id > 100;

select count(*) from hr.employees where job_id='FI_ACCOUNT';

select * from hr.employees where FIRST_NAME  like '   A';

select * from hr.employees where salary between 9000 and 10000;

select FIRST_NAME, Job_id from hr.employees  
order by JOB_ID;

select * from hr.employees where JOB_ID ='IT_PROG';

select * from hr.employees where manager_id > 100;

select count(*) from hr.employees where job_id='FI_ACCOUNT';

select * from hr.employees where FIRST_NAME  like '   A';

select * from hr.employees where salary between 9000 and 10000;

select FIRST_NAME, Job_id from hr.employees where HIRE_DATE='20-AUG-05' 
order by JOB_ID;

select * from hr.employees where JOB_ID ='IT_PROG';

select * from hr.employees where manager_id > 100;

select count(*) from hr.employees where job_id='FI_ACCOUNT';

select * from hr.employees where FIRST_NAME  like '   A';

select * from hr.employees where salary between 9000 and 10000;

select FIRST_NAME, Job_id from hr.employees where HIRE_DATE='20-AUG-05' 
order by JOB_ID;

select FIRST_NAME, Job_id,HIRE_DATE from hr.employees where HIRE_DATE='20-AUG-05' 
order by JOB_ID;

select * from hr.employees where JOB_ID ='IT_PROG';

select * from hr.employees where manager_id > 100;

select count(*) from hr.employees where job_id='FI_ACCOUNT';

select * from hr.employees where FIRST_NAME  like '   A';

select * from hr.employees where salary between 9000 and 10000;

select FIRST_NAME, Job_id from hr.employees where HIRE_DATE='20-AUG-05' 
order by JOB_ID;

select FIRST_NAME, Job_id,HIRE_DATE from hr.employees where HIRE_DATE between '07-JUN-02' 
and '20-AUG-05' order by JOB_ID;


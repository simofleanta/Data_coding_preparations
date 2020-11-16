"""#FIN NAMES OF EMPLOYEES STARTING WITH 'a'"""
SELECT FIRST_NAME FROM HR.EMPLOYEES WHERE FIRST_NAME LIKE 'A%';

"""Find number of employees with salary lower than 17000"""
SELECT COUNT(*) FROM HR.EMPLOYEES WHERE SALARY < 17000;

"""Find employees with the job id it prog"""
select * from hr.employees where JOB_ID ='IT_PROG';

"""Find employees with the manager id >100"""
select * from hr.employees where manager_id > 100;
"""count employees with the manager id is fi accountant"""
select count(*) from hr.employees where job_id='FI_ACCOUNT';
"""details of employee 'a' """
select * from hr.employees where FIRST_NAME  like '   A';

select FIRST_NAME,JOB_ID,HIRE_DATE from hr.EMPLOYEES where HIRE_DATE='20-AUG-05'
ORDER BY JOB_ID
select FIRST_NAME,JOB_ID,HIRE_DATE from hr.EMPLOYEES where HIRE_DATE between '01-aug-04'
and'20-AUG-05' ORDER BY JOB_ID;

"""top 3 rows in a table """
#it may not work on various online machines
select top 3* from hr.employees
where hire_date='16-JUL-05'

"""Select all the different values from the Country column in the Customers table."""

select distinct Country FROM Customers;

"""Select all records where the City column has the value "Berlin"."""

select * from customers where city='Berlin'
select * from customers where not city='Berlin'
"""Select all records where the CustomerID column has the value 32."""
select * from customers where not city= 32


"""Select all records where the City column has the value 'Berlin' and the PostalCode column has the value 12209."""

select * FROM Customers
where  City = 'Berlin'
and postalcode = 12209;



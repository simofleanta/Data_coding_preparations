--CREATE TABLE 
CREATE TABLE BIKES (
    ID INT NOT NULL AUTO INCREMENT,
    Bike_name VARCHAR (255) NOT NULL,
    Sales_rev FLOAT NOT NULL,
    BIKE_ID INT NOT NULL,
    PRIMARY KEY (ID),
    FOREIGN KEY (BIKE_ID) REFERENCES (BIKE_ID)

);
-- transposing all sql queries from the sql live schema hr eployees 

-- How much money invested in two cities employees 
select * from hr.emp_details_view;

select sum(salary) from hr.emp_details_view
where city='Seattle' and city='South San Francisco';

select sum(salary) from hr.emp_details_view
where city='Southlake';

--select desc highest salary from each city 

select city, max(salary) from hr.emp_details_view
group by City
order by (select max (salary) from hr.emp_details_view) desc;
--(select max (salary) from hr.emp_details_view)-innerquery


-- select employees with fi acc jobs from Seattle 

SELECT hr.employees.first_name, hr.employees.salary, hr.emp_details_view.city
FROM hr.employees
Left JOIN hr.emp_details_view ON hr.employees.job_id = hr.emp_details_view.Job_ID
where city='Seattle'
Order by salary desc;

SELECT hr.employees.first_name, hr.employees.salary, hr.emp_details_view.city
FROM hr.employees
Left JOIN hr.emp_details_view ON hr.employees.job_id = hr.emp_details_view.Job_ID
where city='Seattle'
Order by Salary;

SELECT hr.employees.first_name, hr.employees.salary, hr.emp_details_view.city 
FROM hr.employees
LEFT JOIN hr.emp_details_view ON hr.employees.job_id = hr.emp_details_view.Job_ID
order by (select max (salary) from hr.emp_details_view)desc;


-- please create an sql query that presents average salary value for each job id  and each day --inner query
  Select hire_date,job_id,(select avg (salary) where hire_date between hire_date -3 hire_date) from hr.employees;
  --(that hire_date -3 and date means actually each day-there should comeout as 1 value for each item column)
  select orderid,employeeid,shipperid,(select avg(customerid) where orderdate between orderdate-3 and orderdate),
(select avg(customerid) where orderdate between orderdate-2 and orderdate),
(select max(customerid) where orderdate between orderdate-8 and orderdate),
(select sum(customerid) where shipperid=3)
from orders--datas from w3 school


















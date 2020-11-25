 select orderid,employeeid,shipperid,(select avg(customerid) where orderdate between orderdate-3 and orderdate),
(select avg(customerid) where orderdate between orderdate-2 and orderdate),
(select max(customerid) where orderdate between orderdate-8 and orderdate),
(select sum(customerid) where shipperid=3)
from orders--datas from w3 school

-- present avg salary in each city of employees
select city,(select avg(salary) from hr.emp_details_view) from hr.emp_details_view;


--average number of price of products per productname per categoryid  
--1first do the select count and then nest the count into an
--2average select (nested query)
select productname, avg(num_products) from 
   (select productname,categoryid, count(*) as num_products from products
   group by supplierid) sub
group by productname;


--select average number of employee_id per city per job_id 
select city, avg(num_emps) from (
   select employee_id, job_id, count(*) as num_emps 
   from hr.emp_details_view 
   group by city) sub  --for each city 
group by city



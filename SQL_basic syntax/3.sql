REM   Script: Where exists
REM   Need to have common colomns 

select * from hr.emp_details_view;

select * from hr.emp_details_view 
where city='berlin';

select * from hr.emp_details_view 
where city='seatle';

select * from hr.emp_details_view 
where City='Seatle';

select * from hr.emp_details_view 
;

select * from hr.emp_details_view 
where City='Seattle';

select * from hr.emp_details_view 
where City='Seattle' 
group by Job_title;

select * from hr.emp_details_view 
where City='Seattle' 
group by salary;

select * from hr.emp_details_view 
where City='Seattle' 
;

select job_id , city from hr.emp_details_view 
where City='Seattle' 
 
;

select job_id , city from hr.emp_details_view 
where City='Seattle' 
group by country_id;

select job_id , city from hr.emp_details_view 
where City='Seattle' 
group by city 
;

select job_id , city from hr.emp_details_view 
where salary<24000 
group by city 
;

select job_id , city from hr.emp_details_view 
where salary<24000 
 
;

select job_id , city from hr.emp_details_view 
where salary<24000 
group by City 
 
;

select job_id , city from hr.emp_details_view 
where salary<24000 
group by City;

select * from hr.emp_details_view 
where salary<24000 
group by City;

select * from hr.emp_details_view 
where salary<24000 
 
 
;

select (employee_id), city from hr.emp_details_view 
where salary<24000 
 
 
;

select (employee_id), job_id,city from hr.emp_details_view 
where salary<24000 
 
 
 
;

select (employee_id), job_id,city from hr.emp_details_view 
where salary<24000 
GROUP BY City 
 
 
 
;

select (employee_id), job_id,city from hr.emp_details_view 
where salary<24000 
GROUP BY City 
having count(employee_id)>5;

select (employee_id), job_id,city from hr.emp_details_view 
where salary<24000 
having count (employee_id)>5 
 
 
 
;

select job_id,city from hr.emp_details_view 
 
 
 
 
;

select job_id,city  
from hr.emp_details_view 
where exists 
(select city from hr.emp_details_views where city='berlin');

select job_id,city from hr.emp_details_view 
WHERE EXISTS 
(select CITY from hr.emp_details_views WHERE CITY ='Berlin');

select job_id,city from hr.emp_details_view 
WHERE EXISTS 
(select CITY from hr.emp_details_views WHERE CITY ='Seattle');

select job_id,city from hr.emp_details_view 
WHERE EXISTS 
(select CITY from hr.emp_details_views WHERE hr.emp_details_view.CITY ='Seattle');

select job_id,city from hr.emp_details_view 
WHERE EXISTS (select CITY from hr.emp_details_views WHERE hr.emp_details_view.CITY ='Seattle');

select job_id from hr.emp_details_views 
 
 
 
 
 
;

select job_id from hr.emp_details_view 
 
 
 
 
 
;

select job_id from hr.emp_details_view 
where exists(select first_name from hr.emp_details_view where city='seattle');

select job_id from hr.emp_details_view 
where exists(select first_name from hr.emp_details_view where salary<24000);

select job_id, first_name,salary from hr.emp_details_view 
where exists(select first_name from hr.emp_details_view where salary<24000);

select job_id, first_name,salary from hr.emp_details_view 
where exists(select first_name from hr.emp_details_view where salary=9000);

select job_id, first_name,salary from hr.emp_details_view 
where exists(select first_name from hr.emp_details_view where salary=9000);

select job_id, first_name,salary from hr.emp_details_view 
where exists(select first_name from hr.emp_details_view where hr.emp_details_view.salary=9000);

select job_id,salary from hr.emp_details_view 
where exists(select first_name from hr.emp_details_view where hr.emp_details_view.salary=9000);

select job_id,salary from hr.emp_details_view 
where exists(select first_name from hr.emp_details_view where hr.emp_details_view.salary=17000);

select job_id from hr.emp_details_view 
where exists(select first_name from hr.emp_details_view where hr.emp_details_view.salary=17000);

select job_id from hr.emp_details_view 
where exists(select job_id from hr.emp_details_view where hr.emp_details_view.salary=17000);

select job_id 
from hr.employees 
where exists(select job_id from hr.emp_details_view where hr.emp_details_view.salary=17000);

select job_id,salary 
from hr.employees 
where exists(select job_id from hr.emp_details_view where hr.emp_details_view.salary<17000);

select job_id,salary 
from hr.employees 
where exists(select job_id,salary from hr.emp_details_view where hr.emp_details_view.salary<17000);

select job_id,salary 
from hr.employees 
where exists(select job_id,salary from hr.emp_details_view where hr.emp_details_view.salary>17000);

select job_id,salary 
from hr.employees 
where exists(select job_id,salary from hr.emp_details_view where hr.emp_details_view.salary=24000);

select job_id,salary 
from hr.employees 
where exists(select job_id from hr.emp_details_view where hr.emp_details_view.salary=24000);

select job_id,salary 
from hr.employees 
where exists(select job_id from hr.emp_details_view where hr.emp_details_view.salary=hr.employees.salary AND salary<17000);


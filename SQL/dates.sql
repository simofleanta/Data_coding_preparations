-- notes

--date between range (and can be done if need per week or second week)
select * from hr.employees 
where hire_date between '17-JUN-03' and '21-SEP-05'
order by salary desc;

--extract day or month 
SELECT First_Name, job_id,salary, Extract(DAY FROM hire_date) AS hire FROM hr.employees
SELECT First_Name, job_id,salary, Extract(DAY FROM hire_date) AS hire FROM hr.employees
where salary between 9000 and 17000;

--last day of month 

elect LAST_DAY('07-JUN-02') from hr.employees;



SELECT First_Name, Extract(DAY FROM hire_date) AS hire FROM hr.employees;
select sales_revs Extract(Year from Year) as revs_year from bike_case;--repair_phones other data
SELECT DATEDIFF('2017-01-13','2017-01-03') AS DateDiff;

 

--Find the Employees who hired in the Last n months.
--inding the Employees who have been hire in the last n months. 
--Here we get desire output by using TIMESTAMPDIFF() mysql function.

Select *, TIMESTAMPDIFF (month, Hiredate, current_date()) as DiffMonth 
From employees
Where TIMESTAMPDIFF (month, Hiredate, current_date()) 
Between 1 and 5 Order by Hiredate desc; 

--Find the Employees who hired in the Last n days.
--Finding the Employees who have been hire in the last n days. Here we get desire output by using DATEDIFF() mysql function.

Select *, DATEDIFF (current_date(), Hiredate) as DiffDay 
From employees
Where DATEDIFF (current_date(), Hiredate) between 1 and 100 order by Hiredate desc;

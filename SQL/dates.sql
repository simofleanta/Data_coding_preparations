SELECT First_Name, Extract(DAY FROM hire_date) AS hire FROM hr.employees;
select sales_revs Extract(Year from Year) as revs_year from bike_case;--repair_phones other data
SELECT DATEDIFF('2017-01-13','2017-01-03') AS DateDiff;

-- Delete duplicate data from table only first data remains constant.
DELETE M1 
From managers M1, managers M2 
Where M2.Name = M1.Name AND M1.Id>M2.Id; 

--Find the Employees who hired in the Last n months.
--inding the Employees who have been hire in the last n months. 
--Here we get desire output by using TIMESTAMPDIFF() mysql function.

Select *, TIMESTAMPDIFF (month, Hiredate, current_date()) as DiffMonth 
From employees
Where TIMESTAMPDIFF (month, Hiredate, current_date()) 
Between 1 and 5 Order by Hiredate desc; 

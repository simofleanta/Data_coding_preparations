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


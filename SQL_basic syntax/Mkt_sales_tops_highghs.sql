select * from product_sales;

select * ,
extract (year from Product_Date) as Year,
extract (month from Product_Date) as Month,
extract (day from Product_Date) as Day 
from product_sales;

create view mkt_sales as 
select * ,
extract (year from Product_Date) as Year,
extract (month from Product_Date) as Month,
extract (day from Product_Date) as Day 
from product_sales;


select * ,

extract (week FROM product_Date) as week

from product_sales;

create view  mkt_weeks as 

select * ,

extract (week FROM product_Date) as week

from product_sales;

-- highest m in the week 

select * from mkt_weeks;
select week,Products, Margin, Country from mkt_weeks where Margin = (SELECT distinct Margin from mkt_weeks ORDER BY Margin DESC LIMIT 2,1);

create VIEW second_highest_M_week as select week,Products, Margin, Country from mkt_weeks where Margin = (SELECT distinct Margin from mkt_weeks ORDER BY Margin DESC LIMIT 2,1);






-- max profit (inner que)


select *,(SELECT  max(Margin) from product_sales) from product_sales;

create view max_margin as 
select *,(SELECT  max(Margin) from product_sales) from product_sales;



-- Avg Margin of products in each country

select * from mkt_sales;

-- High_day
select Day,Products, Margin, Country from mkt_sales where Margin = (SELECT distinct Margin from mkt_sales ORDER BY Margin DESC LIMIT 0,1);

select Products,Country,( select avg(Margin) from mkt_sales) from mkt_sales;


---- Max for each country
select Margin, Country from mkt_sales where Margin = (SELECT MAX(Margin) from mkt_sales);


--Hihest Margin 
select Products, Margin, Country from mkt_sales where Margin = (SELECT distinct Margin from mkt_sales ORDER BY Margin DESC LIMIT 0,1);

create view Highest_M as select Products, Margin, Country from mkt_sales where Margin = (SELECT distinct Margin from mkt_sales ORDER BY Margin DESC LIMIT 0,1);



--- Top SECOND HIGHEST MARGIN IN PRODUCTS

select Products, Margin, Country from mkt_sales where Margin = (SELECT distinct Margin from mkt_sales ORDER BY Margin DESC LIMIT 1,1);

-- Third higher M + view

select Products, Margin, Country from mkt_sales where Margin = (SELECT distinct Margin from mkt_sales ORDER BY Margin DESC LIMIT 2,1);

create view Third_Highest_M as select Products, Margin, Country from mkt_sales where Margin = (SELECT distinct Margin from mkt_sales ORDER BY Margin DESC LIMIT 2,1);

-- High_Day

select * from mkt_sales;

--4th highest_day
select Day,Products, Margin, Country from mkt_sales where Margin = (SELECT distinct Margin from mkt_sales ORDER BY Margin DESC LIMIT 3,1);

create view 4th_highest_Day as select Day,Products, Margin, Country from mkt_sales where Margin = (SELECT distinct Margin from mkt_sales ORDER BY Margin DESC LIMIT 3,1);

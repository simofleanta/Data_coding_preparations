select* from actual;
select * from target;

--1. Write an SQL query to calculate the actual revenue made 
--compared to the Target revenue &
-- display them in percentages.

--select* tabes
--join tables
--create a join table 
-- using with I will be using the joined table to calculate revenue
-- calculate (target-actual)/100

--2.Write an SQL query to display the top 3 best performing 
--marketing channels based on the actual vs target revenue
-- take the "with" statement with the alias table top_3
--select Marketing channel where Actual revenue >1000
--order mkt channel ASC.

select target.Marketing_Channel,target.Target_Revenue,target.Month,actual.Marketing_Channel,actual.Date,actual.Actual_Revenue
from target
inner join actual ON target.Marketing_Channel=actual.Marketing_Channel;

with joined_table as 
(select target.Marketing_Channel,target.Target_Revenue,target.Month,actual.Date,actual.Actual_Revenue
from target
inner join actual ON target.Marketing_Channel=actual.Marketing_Channel
)
select Marketing_Channel,Month,Date,(Target_Revenue - Actual_Revenue)/100 as Revenue_as_Percentage
from joined_table
Order By Revenue_as_Percentage ASC ;

--2
with top_3 as 
(select target.Marketing_Channel,target.Target_Revenue,target.Month,actual.Date,actual.Actual_Revenue
from target
inner join actual ON target.Marketing_Channel=actual.Marketing_Channel
)
SELECT Date, Month,(Marketing_Channel), (Actual_Revenue - Target_Revenue)/100 as Revenue_Percentage FROM top_3 where Actual_Revenue >1000
ORDER BY Actual_Revenue DESC
limit 3;


with forecast as 
(select target.Marketing_Channel,target.Target_Revenue,target.Month,actual.Date,actual.Actual_Revenue
from target
inner join actual ON target.Marketing_Channel=actual.Marketing_Channel
)

select * from forecast;

--3 try forecast formula
--multiply avg price by expected units to come in the months.

select Month,Date, Marketing_Channel,Actual_Revenue, Avg_px * Expected_Units 
as forecast_r from forecast
ORDER BY Actual_Revenue ASC;


















     

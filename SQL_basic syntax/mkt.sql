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
from joined_table;

--2
with top_3 as 
(select target.Marketing_Channel,target.Target_Revenue,target.Month,actual.Date,actual.Actual_Revenue
from target
inner join actual ON target.Marketing_Channel=actual.Marketing_Channel
)
SELECT distinct (Marketing_Channel), Actual_Revenue FROM top_3 where Actual_Revenue >1000
ORDER BY Actual_Revenue ASC;


with forecast as 
(select target.Marketing_Channel,target.Target_Revenue,target.Month,actual.Date,actual.Actual_Revenue
from target
inner join actual ON target.Marketing_Channel=actual.Marketing_Channel
)

select * from forecast;













     

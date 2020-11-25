--Please review the dataset schema provided on the 'data1' sheet.
--The sheet contains an extract from SQL table. 
--Please create a SQL query that presents retention values for each application on each hardware_platform and for each day,
-- but as an average value of 3 days preceding each given day.
--Desired final schema is: date, application, hardware_platform, retention_day_1_3days_avg, retention_day_3_3days_avg, retention_day_7_3days_avg

Select date,application,hardware_platform,(Select average(retention_day_1) where date between date-3 and date),
--(Select average(retention_day_1) where date between date-3 and date)
 (Select average(retention_day_3) wher e date between date-3 and date), 
 (Select average(retention_day_7) where date between date-3 and date) from data1


 --Please review the dataset schema provided on the 'data2' sheet.
 -- Please create SQL query presenting difference between the last value over time and the first value over time for each player_id 
 --(clarification: not the biggest and the lowest values difference).
--Desired final schema is: player_id, difference

select player_id, (select value from data2 where date in (Select min(date) 
from data_2 where id in (select unique player_id from data_2) - select value from data2 where date in (Select min(date) from data_2 
where id= (select unique player_id from data_2))  from data2


--Using the data set from the 'test1' sheet, create normalized data based on columns A, B and C (each separately).
-- Calculate weighted averages of normalized results based on the following shares:
-- A-50%, B-30%, C-20% share. Please describe the benefits of using normalization.

select D from test_1


--Using the dataset from 'test2', please calculate percentage changes between the data in the “new” column and the data in the “old” column.
 --Please describe which formula/s you used and why.
Select Difference from Test2


--Using the dataset from the 'test 3.1' and 'test3.2' sheets, 
--please create an INDEX formula that will search results from tables in the 'test3.1' sheet of chosen applications (App1, App10 and App 23) and 
--present them in existing tables in the 'test3.2' sheet. 

--excel opp-=(B2-C2)/C2*100
--(old-new)/old*100


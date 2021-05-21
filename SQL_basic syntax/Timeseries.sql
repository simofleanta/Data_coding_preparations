select * from bolt_date;

-- Run date filter 

select Dates,
extract(year FROM Dates) as year,
extract(month FROM  Dates) as month,
extract(day FROM Dates) as day
from bolt_date;

create VIEW Date_filter AS
select Dates,
extract(year FROM Dates) as year,
extract(month FROM  Dates) as month,
extract(day FROM Dates) as day
from bolt_date;


select *,
extract(year FROM Dates) as year,
extract(month FROM  Dates) as month,
extract(day FROM Dates) as day
from bolt_date;

-- run all  

create view B as
select *,
extract(year FROM Dates) as year,
extract(month FROM  Dates) as month,
extract(day FROM Dates) as day
from bolt_date;

SELECT * FROM B where Year=2016 AND month=12 and day=15;

select * from B;

select * from B where day=23;

create view day_23 as select * from B where day=23;
select * from day_23;

select * from B;

select Dates,
    extract(week from Dates) from B;

create view Dates_week as select Dates,
    extract(week from Dates) from B;

select *,
    extract(week from Dates) as week from B;

create view week_bolts as select *,
    extract(week from Dates) as week from B;


select* from week_bolts;











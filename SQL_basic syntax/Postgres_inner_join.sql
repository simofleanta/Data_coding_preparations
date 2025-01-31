
select berry_t.fruitid, berry_t.fruitname, fruit_t.fruitname 
from berry_t
inner join fruit_t
on berry_t.fruitid=fruit_t.fruitid;


--inner join

select sales_c."Client_id", sales_c."Country_code",sales_c."Services",sales_c."Out_px",sales_c."Actual",sales_c."Target_Rev", sales_c."Compare", sales_d."Year" 
from sales_c
inner join sales_d
on sales_c."Country"=sales_d."Country";

--create view

Create view Public.mydata as
select sales_c."Client_id", sales_c."Country_code",sales_c."Services",sales_c."Out_px",sales_c."Actual",sales_c."Target_Rev", sales_c."Compare", sales_d."Year" 
from sales_c
inner join sales_d
on sales_c."Country"=sales_d."Country";

-- extract date 

-- extract date from the view
select *,
extract(year FROM mydata."Year") as year,
extract(month FROM  mydata."Year") as month,
extract(day FROM mydata."Year") as day
from Public.mydata;

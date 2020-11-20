
-- update  increase 3% repair_cost 
update repairs set repair_cost =repair_cost +(repair_cost * 5/100);

--return device id starting with letter W
select device_id from repairs  
where first_name like 'W%';

--return count of the devices with repair cost >5

select count (distinct device_id) from repairs
where repair_cost>=5;


--average repair cost and order by cost

select AVG(repair_cost) from repairs
WHERE device_id LIKE 'X%';

select AVG(repair_cost) from repairs
WHERE date='02.05.20020'
order by repair_cost


--group by device_id

select * from repairs
where repait_cost>8
group by device_id;

--does device_id wyzxq exist in phone deffects?

select * from phone_deffects
WHERE EXISTS 
(select device_id from phone_deffects WHERE device_id ='WYZXQ');

-- inner join between the two tables 
select repairs.device_id., repairs.repair_cost, phone_deffects.date 
from repairs 
inner join phone_deffects
on repairs.device_id=phone_deffects.device_id
order by date;






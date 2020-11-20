
-- update  increase 3% repair_cost 
update repairs set repair_cost =repair_cost +(repair_cost * 5/100);

--return device id starting with letter W
select device_id from repairs  
where first_name like 'W%';




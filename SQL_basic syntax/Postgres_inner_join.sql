
select berry_t.fruitid, berry_t.fruitname, fruit_t.fruitname 
from berry_t
inner join fruit_t
on berry_t.fruitid=fruit_t.fruitid;

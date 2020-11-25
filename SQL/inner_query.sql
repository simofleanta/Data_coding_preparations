 select orderid,employeeid,shipperid,(select avg(customerid) where orderdate between orderdate-3 and orderdate),
(select avg(customerid) where orderdate between orderdate-2 and orderdate),
(select max(customerid) where orderdate between orderdate-8 and orderdate),
(select sum(customerid) where shipperid=3)
from orders--datas from w3 school


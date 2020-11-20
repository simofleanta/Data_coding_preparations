--inner join 

select suppliers.SupplierID, suppliers.SupplierName,suppliers.City,products.ProductName,products.Price 
from suppliers
inner join products
on suppliers.SupplierID=products.SupplierID;

--second max repir/-cost

select max (repair_cost) from repair_cost 
where repair_cost < (select max(repair_cost from repairs);

-- limit

select repair_cost from (select repair_cost fro repairs
order by repair_cost desc limit 2) as repair_cost order by repair_cost limit 1;





--inner join 

select suppliers.SupplierID, suppliers.SupplierName,suppliers.City,products.ProductName,products.Price 
from suppliers
inner join products
on suppliers.SupplierID=products.SupplierID;

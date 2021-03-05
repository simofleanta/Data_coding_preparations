select * from cities;
SELECT * FROM revenue;

select CITIES.CITY_CODE, CITIES.CITY_NAME, REVENUE.CITY_CODE,REVENUE.REVENUE 
FROM CITIES 
INNER JOIN REVENUE ON CITIES.CITY_CODE=REVENUE.CITY_CODE;


with FLOOR_AVG as 
(select  CITIES.CITY_NAME, REVENUE.CITY_CODE,REVENUE.REVENUE 
FROM CITIES 
INNER JOIN REVENUE ON CITIES.CITY_CODE=REVENUE.CITY_CODE
)
SELECT CITY_NAME, floor(Avg(REVENUE)) AS AVERAGE_REVENUE FROM FLOOR_AVG
GROUP BY CITY_NAME;



SELECT country.id, country.country_name,city.id, city.city_name, city.postal_code,city.country_id FROM country 
INNER JOIN city ON country.id=city.id
INNER JOIN customer ON country.id=customer.id;

WITH Joined_t AS 
(SELECT country.id, country.country_name,city.id, city.city_name, city.postal_code,city.country_id 
FROM country 
INNER JOIN city ON country.id=city.id
INNER JOIN customer ON country.id=customer.id)

SELECT city_name, country_name, count(customer_name) WHERE COUNT(customer_name) >(select city_name, AVG(customer_name)FROM Joinet_t GROUP BY city_name)  
ORDER BY country_name ASC;

select * from city;
select * from country;

select* from customer;

-- join 3

SELECT country.id, country.country_name,city.id, city.city_name, customer.id, customer.customer_name FROM country 
INNER JOIN city ON country.id=city.id
INNER JOIN customer ON country.id=customer.id;















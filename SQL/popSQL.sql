-- These queries are meant to be used with the `PopSQL Sample Data` connection
-- Bar chart
select
  country_code,
  count(1)
from city
group by 1
limit 10;

-- Scatter chart
select
  indep_year,
  count(1)
from country
where indep_year > 1800
group by 1;

-- Line chart
with hours as (
  select generate_series(
    date_trunc('hour', now()) - '1 day'::interval,
    date_trunc('hour', now()),
    '1 hour'::interval
  ) as hour
)

select
  hours.hour,
  random() * 1000 as metric
from hours;

-- Other queries
select *
from country;

select *
from city
where country_code = 'USA';
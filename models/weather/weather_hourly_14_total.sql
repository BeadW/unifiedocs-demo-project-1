select *
from {{ source('weather', 'hourly_14_total') }}
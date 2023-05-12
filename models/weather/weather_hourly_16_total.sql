select *
from {{ source('weather', 'hourly_16_total') }}
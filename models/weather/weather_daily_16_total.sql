select *
from {{ source('weather', 'daily_16_total') }}
select *
from {{ source('weather', 'daily_14_total') }}
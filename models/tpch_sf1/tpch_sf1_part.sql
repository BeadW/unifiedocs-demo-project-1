select *
from {{ source('tpch_sf1', 'part') }}
select *
from {{ source('tpch_sf1', 'nation') }}
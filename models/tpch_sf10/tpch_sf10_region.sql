select *
from {{ source('tpch_sf10', 'region') }}
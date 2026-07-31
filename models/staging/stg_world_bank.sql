SELECT
  country_code,
  SAFE_CAST(year AS INT64) AS year,
  SAFE_CAST(gdp_current_usd AS FLOAT64) as gdp_current_usd,
  SAFE_CAST(population AS FLOAT64) AS population,
  SAFE_CAST(gdp_growth_pct AS FLOAT64) AS gdp_growth_pct
FROM {{ source('raw', 'world_bank') }}
WHERE country_code IS NOT NULL
  AND year IS NOT NULL



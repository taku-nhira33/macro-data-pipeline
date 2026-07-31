SELECT
  country_code,
  SAFE_CAST(year AS INT64) as year,
  SAFE_CAST(obs_value AS FLOAT64) AS cpi
FROM {{ source('raw', 'imf') }}
WHERE country_code IS NOT NULL
  AND year IS NOT NULL
  AND coicop_1999 = '_T'
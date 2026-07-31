SELECT *
FROM {{ ref('fct_macroeconomic_indicators') }}
WHERE country_code IS NULL
   OR year IS NULL
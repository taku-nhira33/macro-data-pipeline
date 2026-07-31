SELECT
    country_code,
    year,
    COUNT(*) AS record_count
FROM {{ ref('fct_macroeconomic_indicators') }}
GROUP BY country_code, year
HAVING COUNT(*) > 1
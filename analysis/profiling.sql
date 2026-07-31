SELECT
    COUNT(*) AS total_rows,
    COUNT(DISTINCT country_code) AS countries,
    MIN(year) AS first_year,
    MAX(year) AS last_year,
    ROUND(AVG(gdp_growth_pct), 2) AS avg_gdp_growth,
    ROUND(AVG(gdp_per_capita), 2) AS avg_gdp_per_capita
FROM {{ ref('fct_macroeconomic_indicators') }}
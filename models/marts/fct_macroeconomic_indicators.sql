SELECT
  wb.country_code,
  wb.year,
  wb.gdp_current_usd,
  wb.population,
  wb.gdp_growth_pct,
  imf.cpi,
  SAFE_DIVIDE(wb.gdp_current_usd, wb.population) AS gdp_per_capita,
  CASE
    WHEN wb.gdp_growth_pct IS NULL THEN 'Unknown'
    WHEN wb.gdp_growth_pct > 3 THEN 'High Growth'
    WHEN wb.gdp_growth_pct BETWEEN 0 AND 3 THEN 'Moderate Growth'
    ELSE 'Low/Negative Growth'
  END AS growth_category
FROM {{ ref('stg_world_bank') }} wb
LEFT JOIN {{ ref('stg_imf') }} imf
  ON wb.country_code = imf.country_code
  AND wb.year = imf.year
WHERE wb.year >= 2002
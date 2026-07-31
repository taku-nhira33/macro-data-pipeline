SELECT
    *
FROM (
    SELECT
        COUNT(*) AS total_rows,
        COUNT(cpi) AS matched_rows,
        COUNT(*) - COUNT(cpi) AS unmatched_rows,
        ROUND(100 * COUNT(cpi) / COUNT(*), 2) AS match_percentage
    FROM {{ ref('fct_macroeconomic_indicators') }}
)
WHERE match_percentage < 90 }}
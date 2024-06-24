WITH RankedCounties AS (
    SELECT
        state,
        county,
        countyfips,
        year,
        max_aqi,
        RANK() OVER (PARTITION BY year ORDER BY max_aqi DESC) AS rank
    FROM
        aqifinal
),
Top5Counties AS (
    SELECT
        state,
        county,
        countyfips,
        year
    FROM
        RankedCounties
    WHERE
        rank <= 5
)
SELECT
    state,
    county,
    countyfips AS GeoID,
    COUNT(*) AS top_5_count
FROM
    Top5Counties
GROUP BY
    state,
    county,
    countyfips
ORDER BY
    top_5_count DESC;
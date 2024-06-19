SELECT * FROM public.aqifinal
LIMIT 100

WITH ranked_counties AS (
    SELECT
        state,
        county,
        year,
		median_aqi,
		lat,
		lng,
		population,
        ROW_NUMBER() OVER (PARTITION BY year ORDER BY median_aqi DESC) AS rank
    FROM aqifinal
)
SELECT
    state,
    county,
    year,
    median_aqi,
	lat,
	lng,
	population
FROM ranked_counties
WHERE rank <= 5
ORDER BY year, rank;
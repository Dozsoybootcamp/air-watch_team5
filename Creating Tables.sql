CREATE TABLE AirQualityData2023 (
    State VARCHAR(255),
    County VARCHAR(255),
    Year INT,
    Days_with_AQI INT,
    Good_Days INT,
    Moderate_Days INT,
    Unhealthy_for_Sensitive_Groups_Days INT,
    Unhealthy_Days INT,
    Very_Unhealthy_Days INT,
    Hazardous_Days INT,
    Max_AQI INT,
    Median_AQI INT
);

CREATE TABLE AirQualityData2014 (
    State VARCHAR(255),
    County VARCHAR(255),
    Year INT,
    Days_with_AQI INT,
    Good_Days INT,
    Moderate_Days INT,
    Unhealthy_for_Sensitive_Groups_Days INT,
    Unhealthy_Days INT,
    Very_Unhealthy_Days INT,
    Hazardous_Days INT,
    Max_AQI INT,
    Median_AQI INT
);

INSERT INTO aqifinal
SELECT *
FROM aqi2014final;


CREATE TABLE CountyData (
    County VARCHAR(255),
    State_Name VARCHAR(255),
    Lat FLOAT,
    Lng FLOAT,
    Population INT
);

CREATE TABLE aqi2023final AS
SELECT a.*, c.Lat, c.Lng, c.Population
FROM countydata AS c
JOIN airqualitydata2023 AS a
ON c.county = a.county
AND c.state_name = a.State;

CREATE TABLE aqi2014final AS
SELECT a.*, c.Lat, c.Lng, c.Population 
FROM countydata AS c
JOIN airqualitydata2014 AS a
ON c.county = a.county
AND c.state_name = a.State;

CREATE TABLE states_fips (
    stname VARCHAR(50),
    stfips VARCHAR(2)
);

ALTER TABLE aqi2014final
ADD COLUMN stfips VARCHAR(2),
ADD COLUMN countyfips VARCHAR(5);

UPDATE aqifinal AS a
SET stfips = sf.stfips
FROM states_fips AS sf
WHERE a.state = sf.stname;


CREATE TABLE countyfips (
    state VARCHAR(50),
    county VARCHAR(100),
    countyfips VARCHAR(5)
);

ALTER TABLE aqifinal ADD COLUMN countyfips VARCHAR(3) DEFAULT '';

ALTER TABLE aqifinal
ALTER COLUMN countyfips TYPE varchar(5);

UPDATE aqifinal AS a
SET countyfips = cf.countyfips
FROM countyfips AS cf
WHERE a.stfips = cf.stfips AND a.county = cf.county;

ALTER TABLE countyfips
ADD COLUMN stfips VARCHAR(2);

UPDATE countyfips AS a
SET stfips = sf.stfips
FROM states_fips AS sf
WHERE a.state = sf.stname;
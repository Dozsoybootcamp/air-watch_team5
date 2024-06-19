// Declare global variables
let geojsonLayer;
let selectedYear = 2023; 

// Create map object
let myMap = L.map('map', {zoomControl: false}).setView([37.8, -99], 5);

// Add tile layer to the map
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(myMap);


let zoomHome = L.Control.zoomHome({position: 'topright'});
zoomHome.addTo(myMap);

// Function to load GeoJSON data and add to the map
function loadGeoJSON(year) {
    fetch(`/static/cb_2018_us_county_5m.geojson`)
        .then(response => response.json())
        .then(data => {
            // Remove existing layer if present
            if (geojsonLayer) {
                myMap.removeLayer(geojsonLayer);
            }

            // Add GeoJSON layer with initial styles and event listeners
            geojsonLayer = L.geoJson(data, {
                style: function (feature) {
                    return {
                        color: "#808080",
                        weight: .5,
                        opacity: .1,
                        fillOpacity: 0.01
                    };
                },
                onEachFeature: function (feature, layer) {
                    layer.on('mouseover', function (e) {
                        displayAQIInfo(feature.properties.GEOID, year);
                    });
                }
            }).addTo(myMap);

            // Fetch AQI data after GeoJSON data is loaded
            fetchAQIData(year);
        })

}

// Function to fetch AQI data for a specific year and update county styles
function fetchAQIData(year) {
    fetch(`/static/aqiall.json`)
        .then(response => response.json())
        .then(aqiData => {
            // Filter AQI data for the specified year
            const aqiDataForYear = aqiData.filter(item => item.year === year);

            // Update county styles based on AQI data for the specified year
            geojsonLayer.eachLayer(layer => {
                const countyFIPS = layer.feature.properties.GEOID;

                // Find AQI info that matches county FIPS code
                const aqiInfo = aqiDataForYear.find(item =>
                    item.county_fips === countyFIPS
                );

                if (aqiInfo) {
                    const aqiValue = aqiInfo.max_aqi;
                    const fillColor = getColorForAQI(aqiValue);
                    layer.setStyle({
                        fillColor: fillColor,
                        color: "black",
                        weight: .8,
                        opacity: .5,
                        fillOpacity: 0.7
                    });
                } else {
                    // Set default style if no AQI data found for the county
                    layer.setStyle({
                        fillColor: "white",
                        color: "black",
                        weight: .2,
                        opacity: .2,
                        fillOpacity: 0.1
                    });
                }
            });
        })
        
}

// Function to display AQI information in a popup
function displayAQIInfo(countyFIPS, year) {
    fetch(`/static/aqiall.json`)
        .then(response => response.json())
        .then(aqiData => {
            const aqiInfo = aqiData.find(item => item.county_fips === countyFIPS && item.year === year);

            if (aqiInfo) {
                geojsonLayer.eachLayer(layer => {
                    if (layer.feature.properties.GEOID === countyFIPS) {
                        const countyName = layer.feature.properties.NAME;
                        const bounds = layer.getBounds();
                        const latlng = bounds.getCenter();
                        const popupContent = `
                            <h3>${countyName} County, ${aqiInfo.state}</h3>
                            <p style="line-height: 0.1;"><b>GEOID</b>: ${aqiInfo.county_fips}</p>
                            <p style="line-height: 0.1;"><b>Year</b>: ${aqiInfo.year}</p>
                            <p style="line-height: 0.1;"><b>Max AQI</b>: ${aqiInfo.max_aqi}</p>
                            <p style="line-height: 0.1;"><b>Median AQI</b>: ${aqiInfo.median_aqi}</p>
                            <p style="line-height: 0.1;"><b>Number of Days with Data</b>: ${aqiInfo.days_with_aqi}</p>
                            <p style="line-height: 0.1;"><b>Good Days</b>: ${aqiInfo.good_days}</p>
                            <p style="line-height: 0.1;"><b>Moderate Days</b>: ${aqiInfo.moderate_days}</p>
                            <p style="line-height: 0.1;"><b>Unhealthy for Sensitive</b>: ${aqiInfo.unhealthy_for_sensitive_groups_days}</p>
                            <p style="line-height: 0.1;"><b>Unhealthy Days</b>: ${aqiInfo.unhealthy_days}</p>
                            <p style="line-height: 0.1;"><b>Very Unhealthy Days</b>: ${aqiInfo.very_unhealthy_days}</p>
                            <p style="line-height: 0.1;"><b>Hazardous Days</b>: ${aqiInfo.hazardous_days}</p>
                        `;
                        L.popup()
                            .setLatLng(latlng)
                            .setContent(popupContent)
                            .openOn(myMap);
                    }
                });
            } else {
                geojsonLayer.eachLayer(layer => {
                    if (layer.feature.properties.GEOID === countyFIPS) {
                        const countyName = layer.feature.properties.NAME;
                        const bounds = layer.getBounds();
                        const latlng = bounds.getCenter();
                        const popupContent = `No data found for ${countyName} County`
                        console.error(`No AQI data found for ${countyName} in ${year}`);
                        L.popup()
                        .setLatLng(latlng)
                        .setContent(popupContent)
                        .openOn(myMap);
                    }
                });
            }
        })

}

// Function to get color based on AQI value
function getColorForAQI(aqiValue) {
    if (aqiValue <= 50) {
        return "#00e400"; // Good (green)
    } else if (aqiValue <= 100) {
        return "#ffff00"; // Moderate (yellow)
    } else if (aqiValue <= 150) {
        return "#ffda33"; // Unhealthy for sensitive groups (dark yellow)
    } else if (aqiValue <= 200) {
        return "#ff0000"; // Unhealthy (orange)
    } else if (aqiValue <= 300) {
        return "#ff8d33"; // Very unhealthy (dark orange)
    } else {
        return "#ff0000"; // Hazardous (red)
    }
}
document.getElementById('yearSlider').addEventListener('input', function() {
    let year = parseInt(this.value);
    changeYear(year);
});
// Load initial GeoJSON data for the default year
loadGeoJSON(selectedYear);

function onYearChange(year) {
    let selectedYear = parseInt(year);
    changeYear(selectedYear);
    updateSliderFromDropdown(selectedYear);
}

function changeYear(year) {
    selectedYear = year;
    myMap.closePopup();
    loadGeoJSON(year);
    document.getElementById('selected-year').textContent = year;
    document.getElementById('year-select').value = year;
}
function updateSliderFromDropdown(year) {
    document.getElementById('yearSlider').value = year;
}




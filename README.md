# Air Quality Visualization Project

## Overview
This project aims to provide interactive visualizations of Air Quality Index (AQI) data across all US counties from 2014 to 2023. Developed by the Air Watch team, this platform utilizes data sourced from the Environmental Protection Agency (EPA) to highlight trends, identify areas with poor air quality, and facilitate public awareness and policy-making.

## Tools, Libraries and Languages
- **PgAdmin**: For database management and data loading.
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapping library for Python. Used to interact with the PostgreSQL database.
- **Flask**: Serves the backend and API endpoints.
- **Leaflet:** For creating interactive maps and visualizations.
    - **Render_template**: Used to render HTML templates with dynamic content.
    - **Request**: Used to handle incoming HTTP requests.
- **Chart.js:** For creating chart visualizations.
- **HTML**: Language used to create web pages.
- **CSS**: Language used to define presentation and style of web pages.
- **Prerequisites:**
    - Python 3.8+
    - PostgreSQL 12+

## Data Sources
- **[aqs.epa.gov](https://aqs.epa.gov/aqsweb/airdata/download_files.html#Annual)**: Environmental Protection Agency (EPA) AQI data by county from 2014 to 2023.
- **[census.gov](https://www.census.gov/geographies/mapping-files/time-series/geo/carto-boundary-file.html)**: Cartographic boundary shape file to map every county in the US from the government census.

## Features
- **Interactive Maps**: Visualize AQI data geographically to easily identify areas with varying levels of air pollution.
- **Data Filtering**: Users can filter AQI data by year and county for more detailed exploration.
- **Dynamic Updates**: The platform updates visualizations dynamically based on user interactions.
    
## Instructions
### Coding Files
- **[aqiflask.py](https://github.com/Dozsoybootcamp/air-watch_team5/blob/main/aqiflask.py)**: This code is a Flask web application that connects to a PostgreSQL database to provide Air Quality Index (AQI) data for US counties. It includes the following component:
       - Flask App and Database Connection
       - Main Route
       - AQI Data Routes
       - Chart Route
       - Helper Functions
       
- **[index.html](https://github.com/Dozsoybootcamp/air-watch_team5/blob/main/index.html)**: This HTML sets up a webpage that displays an interactive map, featuring a time-lapse slider, year selection dropdown, and interactive map controls for zooming and resetting the view.
- **[leaflet-timeline-slider.min.js](https://github.com/Dozsoybootcamp/air-watch_team5/blob/main/leaflet-timeline-slider.min.js)**: This code defines a function that creates a new Leaflet control for a timelines slider.
- **[leaflet.zoomhome.css](https://github.com/Dozsoybootcamp/air-watch_team5/blob/main/leaflet.zoomhome.css)**: This CSS code styles the Leaflet map's zoom home control buttons.
- **[leaflet.zoomhome.js](https://github.com/Dozsoybootcamp/air-watch_team5/blob/main/leaflet.zoomhome.css)**: This JavaScript code defines a Leaflet map control extension, L.Control.ZoomHome, to add zoom-in, zoom-out, and "zoom home" buttons to the map interface, allowing users to return to a predefined home view with specified coordinates and zoom level.
- **[loops.js](https://github.com/Dozsoybootcamp/air-watch_team5/blob/main/loop.js)**: This code loops through a list of years, updating the year and a corresponding slider every 4 seconds, with functionality to stop and restart the loop on user interaction or button click, triggered on page load
- **[map.js](https://github.com/Dozsoybootcamp/air-watch_team5/blob/main/leaflet.zoomhome.min.js)**: This code initializes a Leaflet map, loads GeoJSON data to display U.S. counties, updates the map based on Air Quality Index (AQI) data for a selected year, and dynamically adjusts the map layers and popups according to user interactions with a slider and dropdown menu.

### Set Up
1. Clone the Repository to include all files and folder structures.
2. Set Up the Flask Server 
    - In Git bash or Terminal run the Flask server: "python aqiflask.py". This will take you to the home page.
    [INSERT SCREEN SHOT OF HOME PAGE]
    
### View JSON Data
1. From the home page, you can click on any of the years which will take you to a JSON for the data per year.

### View Chart Visualization
1. From the home page,

### Interacting with the Map
1. Viewing the Map
    - From the home page, click on the map preview on the bottom left.
2. Using the Timeline Slider
3. Zoom
4. Home Controls
5. Timelapse

## Ethical Considerations
(WAITING ON RUDI)

## Conclusions
(INSERT AFTER PPT FINAL DRAFT)

## Team Members
Debbie Lim, Duygu Ozso, Owen Wang, Rudi Espinoza


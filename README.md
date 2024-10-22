![LOGO](https://github.com/Dozsoybootcamp/air-watch_team5/blob/main/static/logo_ReadMe.png)
# Air Quality Visualization Project

## Team Members
Debbie Lim, Duygu Ozso, Owen Wang, Rudi Espinoza

## Overview
This project aims to provide user-driven interactive visualizations of Air Quality Index (AQI) data across all US counties from 2014 to 2023. Developed by the Air Watch team, this platform utilizes data sourced from the Environmental Protection Agency (EPA) to highlight trends and identify areas with poor air quality. By mapping and charting the data, we have three main goals. The first is to to quickly identify the national trends year to year. The second is to identify which years we should further investigate. The third is to review the annual trend year by year for the couties with the worst AQI.


## Tools, Libraries and Languages
- **PgAdmin**: For database management and data loading.
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapping library for Python. Used to interact with the PostgreSQL database.
- **Flask**: Serves the backend and API endpoints.
- **Leaflet:** For creating interactive maps and visualizations.
    - **Render_template**: Used to render HTML templates with dynamic content.
    - **Request**: Used to handle incoming HTTP requests.
- **Chart.js:** For creating chart visualizations.
- **HTML**: Language used to create web pages.
- **Javascript**: Language used to add dynamic and interactive scripting to webpages.
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
- **[leaflet.zoomhome.css](https://github.com/Dozsoybootcamp/air-watch_team5/blob/main/leaflet.zoomhome.css)**: This CSS code styles the Leaflet map's zoom home control buttons.
- **[leaflet.zoomhome.js](https://github.com/Dozsoybootcamp/air-watch_team5/blob/main/leaflet.zoomhome.css)**: This JavaScript code defines a Leaflet map control extension, L.Control.ZoomHome, to add zoom-in, zoom-out, and "zoom home" buttons to the map interface, allowing users to return to a predefined home view with specified coordinates and zoom level.
- **[loops.js](https://github.com/Dozsoybootcamp/air-watch_team5/blob/main/loop.js)**: This code loops through a list of years, updating the year and a corresponding slider every 4 seconds, with functionality to stop and restart the loop on user interaction or button click, triggered on page load
- **[map.js](https://github.com/Dozsoybootcamp/air-watch_team5/blob/main/leaflet.zoomhome.min.js)**: This code initializes a Leaflet map, loads GeoJSON data to display U.S. counties, updates the map based on Air Quality Index (AQI) data for a selected year, and dynamically adjusts the map layers and popups according to user interactions with a slider and dropdown menu.

### Set Up
1. Clone the Repository to include all files and folder structures.
2. Import database in PgAdmin using the
3. Set Up the Flask Server 
    - In Git bash or Terminal run the Flask server: "python aqiflask.py". This will take you to the home page.
4. Open [index.html](https://github.com/Dozsoybootcamp/air-watch_team5/blob/main/index.html) with Live Server.
![Figure 1: Home Web Page](https://github.com/Dozsoybootcamp/air-watch_team5/blob/main/static/homepage_screenshot.png)
    
### View JSON Data
1. On the home page, click on any of the years. This will take you to a page with JSON data for the selected year.

### Interacting with the Map
1. Viewing the Map: From the home page, click on the map preview on the bottom left.
2. Timeline Slider: This is an interactive slider to display a specific year. 
3. Time-Lapse: Click the "Start Time-Lapse" button to view a time-lapse of map.
4. Zoom: Use your mouse scroll button to zoom in and out or use the buttons on the top right.
5. Home Controls: Press the home button on the top right to return back to the default view.
6. Return to the Home Page: Click on the "AIR WATCH" logo.
![Figure 3: Interactive Map](https://github.com/Dozsoybootcamp/air-watch_team5/blob/main/static/map_image.jpg)

### View Chart Visualization
1. From the home page, enter a GeoID to generate a line chart displaying the max AQI per year. Note that the GeoIDs are available on the county popup information on the interactive map.
![Figure 2: Charts](https://github.com/Dozsoybootcamp/air-watch_team5/blob/main/static/chart_screenshot.png)

## Ethical Considerations
Throughout this project, Airwatch has considered various ethical aspects to ensure the responsible use of data. One critical aspect is maintaining data accuracy and integrity; hence, we inform our users that 69 max AQI data points exceeded 500, despite the EPA's note that the normalized scale maximum is 500. This transparency helps users understand the limitations and potential anomalies in the dataset. Furthermore, Airwatch is committed to responsible data attribution. On our home page, we clearly attribute our data sources, allowing individuals to verify the data independently. This practice not only enhances the credibility of our project but also promotes trust and accountability in the use of environmental data. By addressing these ethical considerations, we aim to foster a reliable and transparent platform for air quality information.

## Conclusions
Our interactive map and charts tell us a few stories. The first story we learn through the time-lapse tool is that the west coast region suffers the most. California, Washington and Oregon are impacted noticably more than other states. Secondly when investigating a little closer by using the sliding tool or drop down on the map, we can observbe that 2017. 2018, 2020 and 2021 could be further investigated with other factors like wildfires, high temperatures and ozone pollution in order to inform policy change. Lastly, when combining information from a PostgreSQL query to determine the top three counties with worst max AQI, we can review the AQI chart to be informed on the county specific history. 

Overall, the site and visualizations are powerful way for users to understand mass data on max AQI while also being able to see detailed information on a county level.


from flask import Flask, jsonify, render_template, request
from sqlalchemy import create_engine, MetaData

# Create a Flask app
app = Flask(__name__)
# Connect to the database
engine = create_engine("postgresql://postgres:password123@localhost:5433/AQI")
metadata = MetaData()

# Reflect the table
metadata.reflect(bind=engine, only=['aqifinal'])

# Get the reflected table
aqifinal = metadata.tables['aqifinal']

@app.route('/')
def main():
    return """
    <html>
    <head>
        <style>
            body {
                opacity: 0;
                transition: opacity 2s ease-in-out;
                text-align: center;
                background-image: url('https://images.pexels.com/photos/2231630/pexels-photo-2231630.jpeg');
                background-size: cover;
                background-position: center;
                overflow: hidden;
            }

            h1 {
                font-size: 132px;
                font-family: american typewriter, serif;
                color: white;
                -webkit-text-stroke-width: 3px;
                -webkit-text-stroke-color: black;
                display: inline-block;
            }
            h2 {
                font-size: 30px;
                font-family: didot, sans-serif;
                margin-top: -60px;
                color: white;
                -webkit-text-stroke-width: 1px;
                -webkit-text-stroke-color: black;
                display: inline-block;
                background-color: rgba(128, 128, 128, .5);
                padding: 10px 20px;
                border-radius: 10px;
            }
            a {
                text-decoration: none; 
                color: #D6E0FF; 
            }
            a:hover {
                color: blue; /* Change link color on hover */
            }
            .code-box {
                background-color: white;
                padding: 10px;
                border-radius: 30px;
                box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.5);
                display: inline-block;
                text-align: center;
                font-family: calibri, serif;
                font-size: 20px;
                position: relative;
                
            }
            .bottom-right {
                position: absolute;
                bottom: 5px;
                right: 20px;
                font-size: 14px;
                color: white;
                text-align: right;
                font-family: tahoma, serif;
                z-index: 100;
            }
            .bottom {
                position: absolute;
                # bottom: 20px;
                font-size: 15px;
                color: white;
                text-align: center;
                font-family: tahoma, serif;
                width: 100%;
                # margin-top: 2px;
                text-shadow: -1px -1px 0 black, 1px -1px 0 black, -1px 1px 0 black, 1px 1px 0 black;
            }
            .year-link {
                display: inline-block;
                padding: 10px;
                margin: 5px;
                background-color: #48CAE4;
                color: white;
                border-radius: 10px;
                font-family: verdana, serif;
                text-decoration: none;
            }
            .year-link:hover {
                background-color: #007bff;
            }
            .logo {
                position: absolute;
                top: 20px;
                left: 30px;
                width: 150px;
                height: 150px;
                background-color: rgba(0, 0, 0, 1); 
                border-radius: 50%; 
                z-index: 1001; 
                display: flex; 
                justify-content: center; 
                align-items: center; 
            }
            .logo img {
                width: 90%;
                height: 90%;
                display: block;
                margin: 0 auto;
                object-fit: cover; 
                border-radius: 50%; 
            }
            .map-link {
                position: absolute;
                bottom: 160px;
                left: 30px;
                width: 300px;
                height: 300px;
                background-color: rgba(0, 0, 0, .1); 
                border-radius: 50%; 
                z-index: 1001; 
                display: flex; 
                justify-content: center; 
                align-items: center; 
            }
            .map-link img {                
                width: 90%;
                height: 90%;
                display: block;
                margin: 0 auto;
                object-fit: cover; 
                border-radius: 50%; 
            }


            body.loaded {
                opacity: 1;
            }
            .form-group {
                margin-bottom: 20px;
                margin-top: 20px;
            }
            .form-control {
                border-radius: 0; /* Remove default border radius */
            }
            .container {
                position: absolute;
                bottom: 20px;
                left: 50px;
                width: 250px;
                background-color: rgba(255, 255, 255, 0.7);
                padding: 5px;
                border-radius: 10px;
                box-shadow: 0px 0px 10px 0px rgba(0,0,0,0);
            }
                
        </style>
    </head>
    <body>

    <div class="logo">
        <img src="/static/Fulllogo.png" alt="Logo">

    </div>
        <h1>airwatch.</h1><br><br><br><br><br>
        <h2>"Monitoring the Air, Protecting Lives: <br>Airwatch – Your County's Air Quality Companion"</h2>
    <br>


    <div class="code-box">
        <p> &#8592; Obtain the County GEOID from this interactive map! </p>
        <p> &#8601; Enter the GEOID to see how AQI has changed over the years. </p>
        <p> &#8595;Click on these links to see AQI data in the US by county. &#8595;</p>
        <div class="year-link"><a href="/aqi2023"><b>2023</b></a></div>
        <div class="year-link"><a href="/aqi2022"><b>2022</b></a></div>
        <div class="year-link"><a href="/aqi2021"><b>2021</b></a></div>
        <div class="year-link"><a href="/aqi2020"><b>2020</b></a></div>
        <div class="year-link"><a href="/aqi2019"><b>2019</b></a></div><br>
        <div class="year-link"><a href="/aqi2018"><b>2018</b></a></div>
        <div class="year-link"><a href="/aqi2017"><b>2017</b></a></div>
        <div class="year-link"><a href="/aqi2016"><b>2016</b></a></div>
        <div class="year-link"><a href="/aqi2015"><b>2015</b></a></div>
        <div class="year-link"><a href="/aqi2014"><b>2014</b></a></div>

    </div>
    
    <div class="container">
        <form action="/chart" method="POST">
            <div class="form-group">
                <label for="geoid">Enter GeoID:</label>
                <input type="text" class="form-control" id="geoid" name="geoid" required>
            </div>
            <button type="submit" class="btn btn-primary">Generate Chart</button>
        </form>
    </div>

    <div class="map-link">
    <a href="http://127.0.0.1:5500/index.html">
        <img src="/static/map_image.jpg" alt="Map Image">
    </a>
</div>

    <div class="bottom-right">
        <p>Data Source: <a href="https://aqs.epa.gov/aqsweb/airdata/download_files.html"> United States Environmental Protection Agency (EPA) </a></p>
    </div>

    <div class="bottom">
        <p>Rudi Espinoza &nbsp; &nbsp;:&nbsp; &nbsp; Debbie Lim &nbsp; &nbsp;: &nbsp; &nbsp;Duygu Ozsoy &nbsp; &nbsp;: &nbsp; &nbsp;Owen Wang</p>
        
    </div>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            document.body.classList.add('loaded');
        });
    </script>
    </body>
    </html>
    """

@app.route('/aqi2023')
def get_aqi_data2023():

    # Query the data from the table
    query = aqifinal.select().where(aqifinal.c.year == 2023)

    result = engine.connect().execute(query)
    
    # Initialize an empty list to store data
    data = []

    for row in result:
        row_dict = {
            'state': row.state,
            'county': row.county,
            'year': row.year,
            'days_with_aqi': row.days_with_aqi,
            'good_days': row.good_days,
            'moderate_days': row.moderate_days,
            'unhealthy_for_sensitive_groups_days': row.unhealthy_for_sensitive_groups_days,
            'unhealthy_days': row.unhealthy_days,
            'very_unhealthy_days': row.very_unhealthy_days,
            'hazardous_days': row.hazardous_days,
            'max_aqi': row.max_aqi,
            'median_aqi': row.median_aqi,
            'latitude': row.lat,
            'longitude': row.lng,
            'population': row.population,
            'state_fips': row.stfips,
            'county_fips': row.countyfips,
        }
        data.append(row_dict)

    # Close the connection
    engine.connect().close()

    return jsonify(data)

@app.route('/aqi2022')
def get_aqi_data2022():

    # Query the data from the table
    query = aqifinal.select().where(aqifinal.c.year == 2022)

    result = engine.connect().execute(query)
    
    # Initialize an empty list to store data
    data = []

    for row in result:
        row_dict = {
            'state': row.state,
            'county': row.county,
            'year': row.year,
            'days_with_aqi': row.days_with_aqi,
            'good_days': row.good_days,
            'moderate_days': row.moderate_days,
            'unhealthy_for_sensitive_groups_days': row.unhealthy_for_sensitive_groups_days,
            'unhealthy_days': row.unhealthy_days,
            'very_unhealthy_days': row.very_unhealthy_days,
            'hazardous_days': row.hazardous_days,
            'max_aqi': row.max_aqi,
            'median_aqi': row.median_aqi,
            'latitude': row.lat,
            'longitude': row.lng,
            'population': row.population,
            'state_fips': row.stfips,
            'county_fips': row.countyfips,
        }
        data.append(row_dict)

    # Close the connection
    engine.connect().close()

    return jsonify(data)

@app.route('/aqi2021')
def get_aqi_data2021():

    # Query the data from the table
    query = aqifinal.select().where(aqifinal.c.year == 2021)

    result = engine.connect().execute(query)
    
    # Initialize an empty list to store data
    data = []

    for row in result:
        row_dict = {
            'state': row.state,
            'county': row.county,
            'year': row.year,
            'days_with_aqi': row.days_with_aqi,
            'good_days': row.good_days,
            'moderate_days': row.moderate_days,
            'unhealthy_for_sensitive_groups_days': row.unhealthy_for_sensitive_groups_days,
            'unhealthy_days': row.unhealthy_days,
            'very_unhealthy_days': row.very_unhealthy_days,
            'hazardous_days': row.hazardous_days,
            'max_aqi': row.max_aqi,
            'median_aqi': row.median_aqi,
            'latitude': row.lat,
            'longitude': row.lng,
            'population': row.population,
            'state_fips': row.stfips,
            'county_fips': row.countyfips,
        }
        data.append(row_dict)

    # Close the connection
    engine.connect().close()

    return jsonify(data)

@app.route('/aqi2020')
def get_aqi_data2020():

    # Query the data from the table
    query = aqifinal.select().where(aqifinal.c.year == 2020)

    result = engine.connect().execute(query)
    
    # Initialize an empty list to store data
    data = []

    for row in result:
        row_dict = {
            'state': row.state,
            'county': row.county,
            'year': row.year,
            'days_with_aqi': row.days_with_aqi,
            'good_days': row.good_days,
            'moderate_days': row.moderate_days,
            'unhealthy_for_sensitive_groups_days': row.unhealthy_for_sensitive_groups_days,
            'unhealthy_days': row.unhealthy_days,
            'very_unhealthy_days': row.very_unhealthy_days,
            'hazardous_days': row.hazardous_days,
            'max_aqi': row.max_aqi,
            'median_aqi': row.median_aqi,
            'latitude': row.lat,
            'longitude': row.lng,
            'population': row.population,
            'state_fips': row.stfips,
            'county_fips': row.countyfips,
        }
        data.append(row_dict)

    # Close the connection
    engine.connect().close()

    return jsonify(data)

@app.route('/aqi2019')
def get_aqi_data2019():

    # Query the data from the table
    query = aqifinal.select().where(aqifinal.c.year == 2019)

    result = engine.connect().execute(query)
    
    # Initialize an empty list to store data
    data = []

    for row in result:
        row_dict = {
            'state': row.state,
            'county': row.county,
            'year': row.year,
            'days_with_aqi': row.days_with_aqi,
            'good_days': row.good_days,
            'moderate_days': row.moderate_days,
            'unhealthy_for_sensitive_groups_days': row.unhealthy_for_sensitive_groups_days,
            'unhealthy_days': row.unhealthy_days,
            'very_unhealthy_days': row.very_unhealthy_days,
            'hazardous_days': row.hazardous_days,
            'max_aqi': row.max_aqi,
            'median_aqi': row.median_aqi,
            'latitude': row.lat,
            'longitude': row.lng,
            'population': row.population,
            'state_fips': row.stfips,
            'county_fips': row.countyfips,
        }
        data.append(row_dict)
    # Close the connection
    engine.connect().close()

    return jsonify(data)

@app.route('/aqi2018')
def get_aqi_data2018():

    # Query the data from the table
    query = aqifinal.select().where(aqifinal.c.year == 2018)

    result = engine.connect().execute(query)
    
    # Initialize an empty list to store data
    data = []

    for row in result:
        row_dict = {
            'state': row.state,
            'county': row.county,
            'year': row.year,
            'days_with_aqi': row.days_with_aqi,
            'good_days': row.good_days,
            'moderate_days': row.moderate_days,
            'unhealthy_for_sensitive_groups_days': row.unhealthy_for_sensitive_groups_days,
            'unhealthy_days': row.unhealthy_days,
            'very_unhealthy_days': row.very_unhealthy_days,
            'hazardous_days': row.hazardous_days,
            'max_aqi': row.max_aqi,
            'median_aqi': row.median_aqi,
            'latitude': row.lat,
            'longitude': row.lng,
            'population': row.population,
            'state_fips': row.stfips,
            'county_fips': row.countyfips,
        }
        data.append(row_dict)

    # Close the connection
    engine.connect().close()

    return jsonify(data)

@app.route('/aqi2017')
def get_aqi_data2017():

    # Query the data from the table
    query = aqifinal.select().where(aqifinal.c.year == 2017)

    result = engine.connect().execute(query)
    
    # Initialize an empty list to store data
    data = []

    for row in result:
        row_dict = {
            'state': row.state,
            'county': row.county,
            'year': row.year,
            'days_with_aqi': row.days_with_aqi,
            'good_days': row.good_days,
            'moderate_days': row.moderate_days,
            'unhealthy_for_sensitive_groups_days': row.unhealthy_for_sensitive_groups_days,
            'unhealthy_days': row.unhealthy_days,
            'very_unhealthy_days': row.very_unhealthy_days,
            'hazardous_days': row.hazardous_days,
            'max_aqi': row.max_aqi,
            'median_aqi': row.median_aqi,
            'latitude': row.lat,
            'longitude': row.lng,
            'population': row.population,
            'state_fips': row.stfips,
            'county_fips': row.countyfips,
        }
        data.append(row_dict)

    # Close the connection
    engine.connect().close()

    return jsonify(data)

@app.route('/aqi2016')
def get_aqi_data2016():

    # Query the data from the table
    query = aqifinal.select().where(aqifinal.c.year == 2016)

    result = engine.connect().execute(query)
    
    # Initialize an empty list to store data
    data = []

    for row in result:
        row_dict = {
            'state': row.state,
            'county': row.county,
            'year': row.year,
            'days_with_aqi': row.days_with_aqi,
            'good_days': row.good_days,
            'moderate_days': row.moderate_days,
            'unhealthy_for_sensitive_groups_days': row.unhealthy_for_sensitive_groups_days,
            'unhealthy_days': row.unhealthy_days,
            'very_unhealthy_days': row.very_unhealthy_days,
            'hazardous_days': row.hazardous_days,
            'max_aqi': row.max_aqi,
            'median_aqi': row.median_aqi,
            'latitude': row.lat,
            'longitude': row.lng,
            'population': row.population,
            'state_fips': row.stfips,
            'county_fips': row.countyfips,
        }
        data.append(row_dict)

    # Close the connection
    engine.connect().close()

    return jsonify(data)

@app.route('/aqi2015')
def get_aqi_data2015():

    # Query the data from the table
    query = aqifinal.select().where(aqifinal.c.year == 2015)

    result = engine.connect().execute(query)
    
    # Initialize an empty list to store data
    data = []

    for row in result:
        row_dict = {
            'state': row.state,
            'county': row.county,
            'year': row.year,
            'days_with_aqi': row.days_with_aqi,
            'good_days': row.good_days,
            'moderate_days': row.moderate_days,
            'unhealthy_for_sensitive_groups_days': row.unhealthy_for_sensitive_groups_days,
            'unhealthy_days': row.unhealthy_days,
            'very_unhealthy_days': row.very_unhealthy_days,
            'hazardous_days': row.hazardous_days,
            'max_aqi': row.max_aqi,
            'median_aqi': row.median_aqi,
            'latitude': row.lat,
            'longitude': row.lng,
            'population': row.population,
            'state_fips': row.stfips,
            'county_fips': row.countyfips,
        }
        data.append(row_dict)

    # Close the connection
    engine.connect().close()

    return jsonify(data)

@app.route('/aqi2014')
def get_aqi_data2014():

    # Query the data from the table
    query = aqifinal.select().where(aqifinal.c.year == 2014)

    result = engine.connect().execute(query)
    
    # Initialize an empty list to store data
    data = []

    for row in result:
        row_dict = {
            'state': row.state,
            'county': row.county,
            'year': row.year,
            'days_with_aqi': row.days_with_aqi,
            'good_days': row.good_days,
            'moderate_days': row.moderate_days,
            'unhealthy_for_sensitive_groups_days': row.unhealthy_for_sensitive_groups_days,
            'unhealthy_days': row.unhealthy_days,
            'very_unhealthy_days': row.very_unhealthy_days,
            'hazardous_days': row.hazardous_days,
            'max_aqi': row.max_aqi,
            'median_aqi': row.median_aqi,
            'latitude': row.lat,
            'longitude': row.lng,
            'population': row.population,
            'state_fips': row.stfips,
            'county_fips': row.countyfips,
        }
        data.append(row_dict)

    # Close the connection
    engine.connect().close()

    return jsonify(data)

@app.route('/aqiall')
def get_aqi_dataall():

    # Query the data from the table
    query = aqifinal.select()

    result = engine.connect().execute(query)
    
    # Initialize an empty list to store data
    data = []

    for row in result:
        row_dict = {
            'state': row.state,
            'county': row.county,
            'year': row.year,
            'days_with_aqi': row.days_with_aqi,
            'good_days': row.good_days,
            'moderate_days': row.moderate_days,
            'unhealthy_for_sensitive_groups_days': row.unhealthy_for_sensitive_groups_days,
            'unhealthy_days': row.unhealthy_days,
            'very_unhealthy_days': row.very_unhealthy_days,
            'hazardous_days': row.hazardous_days,
            'max_aqi': row.max_aqi,
            'median_aqi': row.median_aqi,
            'latitude': row.lat,
            'longitude': row.lng,
            'population': row.population,
            'state_fips': row.stfips,
            'county_fips': row.countyfips,
        }
        data.append(row_dict)

    # Close the connection
    engine.connect().close()

    return jsonify(data)

@app.route('/chart', methods=['GET', 'POST'])
def chart():
    if request.method == 'POST':
        geoid = request.form['geoid']
        # Fetch chart data based on GeoID
        chart_data = fetch_chart_data(geoid)
        chart_data2 = fetch_name(geoid)
        return render_template('chart.html', geoid=geoid, chart_data=chart_data, chart_data2=chart_data2)
    return render_template('chart.html')


def fetch_name(geoid):
    # Query the data from the table for the specified GeoID
    query = aqifinal.select().where(aqifinal.c.countyfips == geoid).order_by(aqifinal.c.year)

    result = engine.connect().execute(query)
    
    # Fetch the first row (assuming only one row is returned)
    row = result.fetchone()
    
    # Close the result proxy
    result.close()
    
    if row:
        county_name = row.county
        state_name = row.state
    else:
        county_name = 'Unknown'
        state_name = 'Unknown'

    return {
        'county_name': county_name,
        'state_name': state_name,
    }

def fetch_chart_data(geoid):
    # Query the data from the table for the specified GeoID
    query = aqifinal.select().where(aqifinal.c.countyfips == geoid).order_by(aqifinal.c.year)

    result = engine.connect().execute(query)
    
    # Initialize lists to store data for Chart.js

    years = []
    max_aqi_values = []

    for row in result:

        years.append(row.year)
        max_aqi_values.append(row.max_aqi)

    # Close the connection
    engine.connect().close()

    return {

        'years': years,
        'max_aqi_values': max_aqi_values
    }

if __name__ == '__main__':
    app.run(debug=True)

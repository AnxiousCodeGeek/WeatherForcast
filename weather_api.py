# -*- coding: utf-8 -*-
"""weather-api.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GLM1QO2xiq84YL8lyZBue4JlEoS_g2NX
"""

!pip install requests matplotlib

!pip install opencage

!pip install mplcursors

!pip install plotly

from opencage.geocoder import OpenCageGeocode
from google.colab import userdata

# Function to get latitude and longitude using OpenCage API
def get_lat_lon_opencage(location_name):
    key = userdata.get('GEO_KEY')  # Get your OpenCage API key from Colab secrets
    geocoder = OpenCageGeocode(key)
    result = geocoder.geocode(location_name)
    if result and len(result):
        return result[0]['geometry']['lat'], result[0]['geometry']['lng']
    else:
        print("Location not found.")
        return None, None

# Example usage:
location_name = input("Enter your location: ")
lat, lon = get_lat_lon_opencage(location_name)

if lat and lon:
    print(f"Latitude: {lat}, Longitude: {lon}")
else:
    print("Could not retrieve location data.")

import os

# Set your username and password
os.environ['METEOMATICS_USERNAME'] = 'nationalcenterofartificialintelligencesmartcitylab_saud_fatima'
os.environ['METEOMATICS_PASSWORD'] = 'Dbt8FJl71q'

import requests
from opencage.geocoder import OpenCageGeocode
import plotly.graph_objects as go
from google.colab import userdata
from datetime import datetime, timedelta
import os

# Get username and password from environment variables
username = os.getenv('METEOMATICS_USERNAME')
password = os.getenv('METEOMATICS_PASSWORD')

# Function to get latitude and longitude using OpenCage API
def get_lat_lon_opencage(location_name):
    key = userdata.get('GEO_KEY')  # Get your OpenCage API key from Colab secrets
    geocoder = OpenCageGeocode(key)
    result = geocoder.geocode(location_name)
    if result and len(result):
        return result[0]['geometry']['lat'], result[0]['geometry']['lng']
    else:
        print("Location not found.")
        return None, None

# Function to fetch weather data from Meteomatics API for the next days
def fetch_weather_data(lat, lon, days=7):
    # Construct the date range
    start_date = datetime.utcnow()
    end_date = start_date + timedelta(days=days)

    # Create URL with date range and parameters
    url = f"https://api.meteomatics.com/{start_date.isoformat()}Z--{end_date.isoformat()}Z:PT1H/t_2m:C,precip_24h:mm,wind_speed_10m:ms/{lat},{lon}/json"
    response = requests.get(url, auth=(username, password))

    # Check for a successful response
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Failed to fetch data:", response.status_code, response.text)
        return None

# User input for location
location_name = input("Enter your location: ")
lat, lon = get_lat_lon_opencage(location_name)

if lat and lon:
    # Fetch data for the next 7 days
    data = fetch_weather_data(lat, lon, days=7)

    if data:
        # Parsing the response data
        times = []
        temps = []
        precip = []
        wind_speed = []

        for entry in data['data'][0]['coordinates'][0]['dates']:
            times.append(entry['date'])
            temps.append(entry['value'])

        for entry in data['data'][1]['coordinates'][0]['dates']:
            precip.append(entry['value'])

        for entry in data['data'][2]['coordinates'][0]['dates']:
            wind_speed.append(entry['value'])

        # Create an interactive plot using Plotly
        fig = go.Figure()

        # Adding temperature trace
        fig.add_trace(go.Scatter(
            x=times,
            y=temps,
            mode='lines+markers',
            name='Temperature (°C)',
            marker=dict(color='red'),
            text=[f'Date: {datetime.fromisoformat(t[:-1])} \nTemperature: {temp} °C' for t, temp in zip(times, temps)],  # Hover text with date and temperature
            hoverinfo='text'
        ))

        # Adding precipitation trace
        fig.add_trace(go.Scatter(
            x=times,
            y=precip,
            mode='lines+markers',
            name='Precipitation (mm)',
            marker=dict(color='blue'),
            text=[f'Date: {datetime.fromisoformat(t[:-1])} \nPrecipitation: {p} mm' for t, p in zip(times, precip)],  # Hover text with date and precipitation
            hoverinfo='text'
        ))

        # Adding wind speed trace
        fig.add_trace(go.Scatter(
            x=times,
            y=wind_speed,
            mode='lines+markers',
            name='Wind Speed (m/s)',
            marker=dict(color='green'),
            text=[f'Date: {datetime.fromisoformat(t[:-1])} \nWind Speed: {ws} m/s' for t, ws in zip(times, wind_speed)],  # Hover text with date and wind speed
            hoverinfo='text'
        ))

        # Update layout
        fig.update_layout(
            title=f"Weather Forecast for {location_name}",
            xaxis_title='Date and Time',
            yaxis_title='Values',
            xaxis_tickangle=-45,
            template='plotly_white',
            showlegend=True
        )

        # Show the plot
        fig.show()
else:
    print("Error retrieving latitude and longitude.")


# Weather Forcast Visualizer
This Python script fetches and visualizes weather data for a specified location using the Meteomatics API and the OpenCage Geocoding API. The script allows users to enter a location, retrieves the corresponding latitude and longitude, and fetches weather data including temperature, precipitation, and wind speed for the next seven days.

## Features
- **Location Input**: Users can input any location to retrieve weather data.
- **API Integration**: Utilizes Meteomatics for weather data and OpenCage for geocoding.
- **Interactive Visualization**: Displays temperature, precipitation, and wind speed data in an interactive Plotly graph with hover functionality to show detailed information (date and respective values).

## Explanation
### 1. Importing Libraries
The script begins by importing necessary libraries: ```requests```, 

```requests```: For making HTTP requests to the weather API.
```matplotlib.pyplot``` and ```mplcursors```: For plotting (not utilized in this version).
```opencage.geocoder```: For converting location names into latitude and longitude coordinates.
```plotly.graph_objects```: For creating interactive visualizations.
```google.colab.userdata```: For accessing user data in Google Colab (if applicable).
```datetime```: For handling date and time operations.
```os```: For accessing environment variables.

### 2. Environment Variables Setup
The script retrieves the username and password for the Meteomatics API from environment variables. This is done to securely store sensitive information without hardcoding it into the script.

### 3. Function: ```get_lat_lon_opencage()```
This function is responsible for:

 - Accepting a location name as input.
 - Using the OpenCage API to geocode the location, returning the latitude and longitude.
 - If the location is found, it returns the coordinates; otherwise, it prints an error message.
   
### 4. Function: ```fetch_weather_data()```
This function fetches weather data for the specified latitude and longitude:

 - Constructs the URL for the Meteomatics API request, including the desired date range (the next 7 days).
 - Makes an HTTP GET request to the API.
 - Checks for a successful response and returns the JSON data containing weather information.
   
### 5. User Input for Location
The script prompts the user to input a location name. It calls the ```get_lat_lon_opencage``` function to retrieve the corresponding latitude and longitude coordinates.

### 6. Fetching Weather Data
If the coordinates are successfully obtained:

 - The script calls the fetch_weather_data function to retrieve weather data for the next 7 days based on the coordinates.
 - It parses the response to extract time, temperature, precipitation, and wind speed values.
   
### 7. Data Visualization with Plotly
Interactive plot is created using Plotly:

 - **Temperature Trace**: Displays temperature data with hover functionality that shows date, time, and temperature.
 - **Precipitation Trace**: Displays precipitation data with hover functionality that shows date, time, and precipitation amount.
 - **Wind Speed Trace**: Displays wind speed data with hover functionality that shows date, time, and wind speed.
   
### 8. Displaying the Plot
Finally, the function ```fig.show()``` is called to display the interactive weather forecast visualization.

## Conclusion
This script provides a comprehensive way to visualize weather data interactively based on user-defined locations, utilizing external APIs for data retrieval and Plotly for visualization.

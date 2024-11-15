from django.shortcuts import render
import random

# Function to generate random weather data
def get_weather_data(location):
    temperature = random.uniform(-10, 40)  # Random temperature
    humidity = random.randint(0, 100)      # Random humidity
    wind_speed = random.uniform(0, 25)     # Random wind speed
    
    return {
        "location": location,
        "temperature": round(temperature, 2),
        "humidity": humidity,
        "wind_speed": round(wind_speed, 2)
    }

# Function to generate random air quality data
def get_air_quality_data(location):
    aqi = random.randint(0, 500)          # Random AQI
    pm25 = random.uniform(0, 300)         # Random PM2.5
    pm10 = random.uniform(0, 400)         # Random PM10
    
    return {
        "location": location,
        "aqi": aqi,
        "pm25": round(pm25, 2),
        "pm10": round(pm10, 2)
    }

# View function to render the dashboard
def dashboard(request):
    location = "Sample City"
    weather_data = get_weather_data(location)
    air_quality_data = get_air_quality_data(location)
    
    # Combine both weather and air quality data
    context = {
        "weather_data": weather_data,
        "air_quality_data": air_quality_data
    }
    
    return render(request, 'dashboard.html', context)

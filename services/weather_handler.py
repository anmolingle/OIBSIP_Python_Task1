import requests
from config import WEATHER_API_KEY, WEATHER_BASE_URL

def get_current_weather(city_name):
    
    
    if not WEATHER_API_KEY or WEATHER_API_KEY == "<YOUR_OPENWEATHERMAP_API_KEY>":
        return "Weather API key is not configured. Please check config.py."

    params = {
        'q': city_name,
        'appid': WEATHER_API_KEY,
        'units': 'metric'  
    }
    
    try:
        response = requests.get(WEATHER_BASE_URL, params=params)
        response.raise_for_status() 
        data = response.json()
        
        if data['cod'] != 200:
            return f"Could not find weather for {city_name}."

        temp_c = data['main']['temp']
        description = data['weather'][0]['description']
        
        return f"The current temperature in {city_name} is {temp_c}°C with {description}."
        
    except requests.exceptions.RequestException as e:
        print(f"Weather API request error: {e}")
        return "I am having trouble connecting to the weather service."
    except KeyError:
        return "Weather data format is incorrect."

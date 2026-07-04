import requests

def get_weather_by_city(city_name):
    """
    Fetch current weather conditions (temperature, humidity, precipitation) for a given city.
    Uses the free, keyless Open-Meteo APIs.
    
    Returns:
        dict: A dictionary containing temperature, humidity, rainfall, city name, and country,
              or None if the city was not found or an error occurred.
    """
    if not city_name or not city_name.strip():
        return None
        
    try:
        # Step 1: Geocoding API to get Lat/Lon
        geocode_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name.strip()}&count=1&language=en&format=json"
        geo_response = requests.get(geocode_url, timeout=10)
        geo_response.raise_for_status()
        geo_data = geo_response.json()
        
        if "results" not in geo_data or len(geo_data["results"]) == 0:
            print(f"City '{city_name}' not found.")
            return None
            
        location = geo_data["results"][0]
        lat = location["latitude"]
        lon = location["longitude"]
        display_name = f"{location.get('name')}, {location.get('admin1', '')} ({location.get('country_code', '').upper()})"
        
        # Step 2: Weather Forecast API to get Current Temp & Humidity
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,precipitation&timezone=auto"
        weather_response = requests.get(weather_url, timeout=10)
        weather_response.raise_for_status()
        weather_data = weather_response.json()
        
        if "current" not in weather_data:
            print("Current weather data not available.")
            return None
            
        current = weather_data["current"]
        
        # Open-Meteo precipitation is typically in mm for the last hour
        # Crop Recommendation dataset 'rainfall' is seasonal average, but we can return this current hourly precipitation or a reasonable estimation
        return {
            "city": location.get("name"),
            "full_name": display_name,
            "latitude": lat,
            "longitude": lon,
            "temperature": current.get("temperature_2m"),
            "humidity": current.get("relative_humidity_2m"),
            "rainfall": current.get("precipitation", 0.0)
        }
        
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return None

if __name__ == "__main__":
    # Test lookup
    test_city = "Mumbai"
    print(f"Testing weather lookup for '{test_city}'...")
    result = get_weather_by_city(test_city)
    if result:
        print("Success!")
        print(f"Location: {result['full_name']}")
        print(f"Temp: {result['temperature']} °C")
        print(f"Humidity: {result['humidity']} %")
        print(f"Current Precipitation: {result['rainfall']} mm")
    else:
        print("Failed to get weather.")

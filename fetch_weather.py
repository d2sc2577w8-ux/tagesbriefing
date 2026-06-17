import json
import urllib.request
from datetime import datetime, timezone

# Koordinaten Zürich
LAT = 47.3769
LON = 8.5417

def fetch_weather():
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={LAT}&longitude={LON}"
        "&current=temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code,"
        "surface_pressure,visibility,precipitation_probability,uv_index"
        "&hourly=precipitation_probability,uv_index"
        "&daily=temperature_2m_max,temperature_2m_min,weather_code,uv_index_max,precipitation_probability_max"
        "&timezone=Europe%2FZurich&forecast_days=4"
    )
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read())
    return data

def main():
    weather = fetch_weather()
    result = {
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "weather": weather,
    }
    with open("weather.json", "w") as f:
        json.dump(result, f, indent=2)
    print("Wetterdaten gespeichert in weather.json")

if __name__ == "__main__":
    main()

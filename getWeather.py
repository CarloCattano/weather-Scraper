#Usage example
from weather_scrap import WeatherScrap
import json

weather = WeatherScrap()

print(json.dumps(weather.get_weather_data(), indent=4, sort_keys=True, separators=(',', ': ')))
print(json.dumps(weather.get_next_days(), indent=4, sort_keys=True, separators=(',', ': ')))
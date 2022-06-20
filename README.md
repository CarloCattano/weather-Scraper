#### Simple weather information scraper from google
it will return basic information about the weather as seen in google search, depending on the location where the query is originated from.

requirements:
```
pip install beautifulsoup4
```
usage:
```shell
python example.py
```
```json
{
    "dayhour": "Monday 10:00",
    "humidity": "94%",
    "precipitation": "61%",
    "region": "Berliner Innenstadt, Berlin",
    "temp_now": "14",
    "time": 1.2362031936645508,
    "weather_now": "Light rain showers",    
    "wind": "5 km/h"
}
```


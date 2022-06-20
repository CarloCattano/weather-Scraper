from bs4 import BeautifulSoup as bs
import requests
import time

class WeatherScrap:
    def __init__(self):
        self.USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
        self.LANGUAGE = "en-US,en;q=0.5"
        self.next_days = []

    def get_weather_data(self):
        start_time = time.time()
        session = requests.Session()
        session.headers['User-Agent'] = self.USER_AGENT
        session.headers['Accept-Language'] = self.LANGUAGE
        session.headers['Content-Language'] = self.LANGUAGE
        html = session.get("https://www.google.com/search?lr=lang_en&ie=UTF-8&q=weather&hl=en",timeout=1)
        soup = bs(html.text, "html.parser")

        result = {}
        result['region'] = soup.find("div", attrs={"id": "wob_loc"}).text
        result['temp_now'] = soup.find("span", attrs={"id": "wob_tm"}).text
        result['dayhour'] = soup.find("div", attrs={"id": "wob_dts"}).text
        result['weather_now'] = soup.find("span", attrs={"id": "wob_dc"}).text
        result['precipitation'] = soup.find("span", attrs={"id": "wob_pp"}).text
        result['humidity'] = soup.find("span", attrs={"id": "wob_hm"}).text
        result['wind'] = soup.find("span", attrs={"id": "wob_ws"}).text
        next_days = []
        days = soup.find("div", attrs={"id": "wob_dp"})

        for day in days.findAll("div", attrs={"class": "wob_df"}):
            day_name = day.findAll("div")[0].attrs['aria-label']
            weather = day.find("img").attrs["alt"]
            temp = day.findAll("span", {"class": "wob_t"})
            max_temp = temp[0].text
            min_temp = temp[2].text
            next_days.append({"name": day_name, "weather": weather, "max_temp": max_temp, "min_temp": min_temp})
            self.next_days = next_days
        
        end_time = time.time()
        result['time'] = end_time - start_time
        return result

    def get_next_days(self):
        return self.next_days
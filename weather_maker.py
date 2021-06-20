# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import datetime
import re
import requests

from setting import WEATHER_KEY


class WeatherMaker:

    def collect_day_weather(self, date, weather_day_summary, temp):
        """
        :param date: Date in datetime.date
        :param weather_day_summary: str weather
        :param temp: int temp
        :return: dict
        """
        for weather in WEATHER_KEY:
            if re.search(weather['re_weather'], weather_day_summary):
                weather_day = {
                    'weather': weather['weather'],
                    'temp': int(temp[:-1]),
                    'date': date,
                }
                return weather_day

    def get_weather_day(self, date):
        """
        Get weather from web
        :param date: date in str
        :return: dict
        """
        date_str = date.strftime('%Y-%m-%d')
        html = requests.get(f'https://darksky.net/details/55.7962,49.1119/{date_str}/si12/en')
        if html.status_code == 200:
            soup = BeautifulSoup(html.text, features='html.parser')
            temp = soup.find_all('span', {'class': 'temp'})[1].text
            weather_day_summary = soup.find_all('p', {'id': 'summary'})[0].text
            return self.collect_day_weather(date=date, temp=temp, weather_day_summary=weather_day_summary)

    def get_weather_period(self, date_from, date_to):
        """
        :param date_from: Start period datetime.date
        :param date_to: End period datetime.date
        :return: Lsit
        """
        journal_weather = []
        delta_days = date_to - date_from
        for day in range(delta_days.days + 1):
            date = date_from + datetime.timedelta(days=day)
            journal_weather.append(self.get_weather_day(date=date))
        return journal_weather

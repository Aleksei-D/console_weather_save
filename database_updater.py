# -*- coding: utf-8 -*-
import datetime

from playhouse.db_url import connect

import models
from weather_maker import WeatherMaker


class DatabaseUpdater:
    def __init__(self, db_url='sqlite:///weather_calendar.db'):
        """
        initialize DB
        :param db_url: путь до БД
        """
        self.database = connect(db_url)
        models.database_proxy.initialize(self.database)
        self.WeatherBase = models.WeatherBase
        self.WeatherBase.create_table()

    def record_weather(self, date_from, date_to):
        """
        Запись в БД показания погоды
        :param date_from: дата начала периода в формате datetime.date
        :param date_to: дата конца периода в формате datetime.date
        :return: None
        """
        calendar = WeatherMaker().get_weather_period(date_from=date_from, date_to=date_to)
        for day in calendar:
            if self.WeatherBase.select().where(self.WeatherBase.date == day['date']):
                self.WeatherBase.update(
                    temp=day['temp'],
                    weather=day['weather']
                ).where(self.WeatherBase.date == day['date']).execute()
            else:
                self.WeatherBase.create(
                    date=day['date'],
                    temp=day['temp'],
                    weather=day['weather']
                )

    def get_weather(self, date_from, date_to):
        """
        Получить из БД погоды
        :param date_from: дата начала периода в формате datetime.date
        :param date_to: дата конца периода в формате datetime.date
        :return: отсортированные по дате данные из БД
        """
        self.check_and_update_bd(date_from, date_to)
        weather_calendar = self.WeatherBase.select().where(
            (self.WeatherBase.date >= date_from) & (self.WeatherBase.date <= date_to)
        )
        return weather_calendar.order_by(self.WeatherBase.date)

    def check_and_update_bd(self, date_from, date_to):
        """
        Проверка и обновление погоды в БД
        :param date_from: дата начала периода в формате datetime.date
        :param date_to: дата конца периода в формате datetime.date
        :return: None
        """
        delta = date_to - date_from
        if delta == 0:
            day_weather = self.WeatherBase.select().where(self.WeatherBase.date == date_from)
            if day_weather.exists() is False:
                self.record_one_day_in_bd(date=date_from)
        else:
            for day in range(delta.days + 1):
                date = date_from + datetime.timedelta(days=day)
                day_weather = self.WeatherBase.select().where(self.WeatherBase.date == date)
                if day_weather.exists() is False:
                    self.record_one_day_in_bd(date)

    def record_one_day_in_bd(self, date):
        """
        Создание одной записи в БД
        :param date: дата н в формате datetime.date
        :return: None
        """
        day = WeatherMaker().get_weather_day(date=date)
        self.WeatherBase.create(
            date=day['date'],
            temp=day['temp'],
            weather=day['weather']
        )

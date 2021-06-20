# -*- coding: utf-8 -*-
import os

import cv2

from setting import POSTCARD_TEMPLATE, WEATHER_IMAGES
from database_updater import DatabaseUpdater


class ImageMaker:
    def __init__(self, dirname=None):
        """
        :param dirname: Путь до папки с карточками
        """
        self.dirname = 'postcard_weather' if dirname is None else dirname

    def get_text_to_print(self, day):
        """
        :param day: day of the BD
        :return: Dict for print in cv2
        """
        text_to_print = [
            {'text': day.date.strftime('%d-%m-%Y'), 'coord': (40, 230)},
            {'text': str(day.temp) + ' C', 'coord': (300, 40)},
            {'text': day.weather.capitalize(), 'coord': (300, 80)},
        ]
        return text_to_print

    def draw_image(self, day):
        """
        Drawing weather-card
        :param day: day of the BD
        :return: None
        """
        image_cv2 = cv2.imread(POSTCARD_TEMPLATE)
        make_background = WEATHER_IMAGES[day.weather]['background']
        icon = WEATHER_IMAGES[day.weather]['icon']
        icon_cv2 = cv2.imread(icon)
        make_background(image_cv2)
        text_to_print = self.get_text_to_print(day)
        for text in text_to_print:
            cv2.putText(image_cv2, text['text'], text['coord'], cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 1)
        image_cv2[:icon_cv2.shape[0], :icon_cv2.shape[1]] = icon_cv2
        fullpath_name = f'{self.dirname}/{text_to_print[0]["text"]}.jpg'
        if not os.path.exists(self.dirname):
            os.makedirs(self.dirname)
        cv2.imwrite(fullpath_name, image_cv2)

    def get_images(self, date_from, date_to):
        """
        :param date_from: дата начала периода в формате datetime.date
        :param date_to:  дата конца периода в формате datetime.date
        :return: None
        """
        weather_calendar = DatabaseUpdater().get_weather(date_from, date_to)
        for day in weather_calendar:
            self.draw_image(day)

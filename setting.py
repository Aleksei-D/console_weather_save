# -*- coding: utf-8 -*-

import background_handler as bg

WEATHER_IMAGES = {
    'облачно': {
        'background': bg.make_background_cloudy,
        'icon': 'python_snippets/external_data/weather_img/cloud.jpg'
    },
    'ясно': {
        'background': bg.make_background_clear,
        'icon': 'python_snippets/external_data/weather_img/sun.jpg'
    },

    'дождь': {
        'background': bg.make_background_rain,
        'icon': 'python_snippets/external_data/weather_img/rain.jpg',
    },
    'пасмурно': {
        'background': bg.make_background_overcast,
        'icon': 'python_snippets/external_data/weather_img/overcast.jpg',

    },
    'туман': {
        'background': bg.make_background_foggy,
        'icon': 'python_snippets/external_data/weather_img/foggy.jpg',
    },
    'снег': {
        'background': bg.make_background_snow,
        'icon': 'python_snippets/external_data/weather_img/snow.jpg'
    },
    'ветрено': {
        'background': bg.make_background_windy,
        'icon': 'python_snippets/external_data/weather_img/windy.jpg'
    },
}

WEATHER_KEY = [
    {'re_weather': r'([cC]loudy)', 'weather': 'облачно'},
    {'re_weather': r'[Cc]lear', 'weather': 'ясно'},
    {'re_weather': r'[Rr]ain', 'weather': 'дождь'},
    {'re_weather': r'[Oo]vercast', 'weather': 'пасмурно'},
    {'re_weather': r'[fF]oggy', 'weather': 'туман'},
    {'re_weather': r'[sS]now', 'weather': 'снег'},
    {'re_weather': r'[Ww]indy', 'weather': 'ветрено'},

]

POSTCARD_TEMPLATE = 'python_snippets/external_data/probe.jpg'

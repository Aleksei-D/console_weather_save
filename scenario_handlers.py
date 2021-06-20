# -*- coding: utf-8 -*-
import datetime
import re

from database_updater import DatabaseUpdater
from image_maker import ImageMaker

re_date = r'(?<!\d)(?:0?[1-9]|[12][0-9]|3[01])-(?:0?[1-9]|1[0-2])-(?:19[0-9][0-9]|20[012][0-9])(?!\d)'

HANDLER_HELPS = {
    'record_weather': DatabaseUpdater().record_weather,
    'get_weather': DatabaseUpdater().get_weather,
    'get_images': ImageMaker().get_images,
}


def handler_from_date(user_input, context):
    """
    :param user_input: User's input
    :param context: dict
    :return: True or False
    """
    date_early = datetime.datetime.now() - datetime.timedelta(days=90)
    date_future = datetime.datetime.now() + datetime.timedelta(days=6)
    date_early_str = date_early.strftime('%d-%m-%Y')
    date_future_str = date_future.strftime('%d-%m-%Y')
    if re.search(re_date, user_input):
        date_str = re.search(re_date, user_input)[0]
        try:
            date = datetime.datetime.strptime(date_str, '%d-%m-%Y').date()
        except Exception:
            context['date_from_fail_answer'] = f'Неверная дата. Вы указали дату которой не существует'
            return False
        else:
            if date < date_early.date():
                context['date_from_fail_answer'] = f'Неверная дата. Укажите дату не ранее {date_early_str}'
                return False
            elif date > date_future.date():
                context['date_from_fail_answer'] = f'Неверная дата. Укажите дату не позднее {date_future_str}'
                return False
            else:
                context['date_from'] = date
                context['date_from_str'] = date_str
                return True
    else:
        context['date_from_fail_answer'] = 'Неверная дата. Укажите дату в формате дд-мм-гггг'
        return False


def handler_to_date(user_input, context):
    """
    :param user_input: User's input
    :param context: dict
    :return: True or False
    """
    now = datetime.datetime.now()
    date_future = (now + datetime.timedelta(days=6)).date()
    date_future_str = date_future.strftime('%d-%m-%Y')
    date_from_str = context["date_from"].strftime('%d-%m-%Y')
    if re.search(re_date, user_input):
        date_str = re.search(re_date, user_input)[0]
        try:
            date = datetime.datetime.strptime(date_str, '%d-%m-%Y').date()
        except Exception:
            context['date_to_fail_answer'] = f'Неверная дата. Вы указали дату которой не существует'
            return False
        else:
            if date < context['date_from']:
                context['date_to_fail_answer'] = f'Неверная дата. Укажите дату не ранее {date_from_str}'
                return False
            else:
                if date > date_future:
                    context['date_to_fail_answer'] = f'Неверная дата. Укажите дату не позднее {date_future_str}'
                    return False
                else:
                    context['date_to'] = date
                    context['date_to_str'] = date_str
                    help_handler = HANDLER_HELPS[context['scenario_name']]
                    weather_calendar = help_handler(date_from=context['date_from'], date_to=context['date_to'])
                    if weather_calendar:
                        context['weather_calendar'] = ';\n'.join([
                            '   '.join([day.date.strftime('%d-%m-%Y'), str(day.temp), day.weather])
                            for day in weather_calendar
                        ])
                    return True
    else:
        context['date_to_fail_answer'] = 'Неверная дата. Укажите дату в формате дд-мм-гггг'
        return False


def handler_exit(user_input, context):
    """
    Exit
    :param user_input: User's input
    :param context: dict
    :return: False
    """
    context['cycle'] = False
    return True

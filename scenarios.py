# -*- coding: utf-8 -*-


KEY_SCENARIO = {
    '1': 'record_weather',
    '2': 'get_weather',
    '3': 'get_images',
}

SCENARIOS = {
    'record_weather': {
        'first_step': 'step1',
        'steps': {
            'step1': {
                'text': 'Введите c какой даты хотите загрузить в БД показания погоды',
                'failure_text': '{date_from_fail_answer}',
                'handler': 'handler_from_date',
                'next_step': 'step2',
            },
            'step2': {
                'text': 'Введите по какую дату хотите загрузить в БД показания погоды',
                'failure_text': '{date_to_fail_answer}',
                'handler': 'handler_to_date',
                'next_step': 'step3',
            },
            'step3': {
                'text': 'Показания погоды с {date_from_str} по {date_to_str} записаны в базу данных!',
                'failure_text': None,
                'handler': None,
                'next_step': None,
            },
        }
    },
    'get_weather': {
        'first_step': 'step1',
        'steps': {
            'step1': {
                'text': 'Введите c какой даты хотите получить показания погоды из БД',
                'failure_text': '{date_from_fail_answer}',
                'handler': 'handler_from_date',
                'next_step': 'step2',
            },
            'step2': {
                'text': 'Введите по какую дату хотите получить показания погоды',
                'failure_text': '{date_to_fail_answer}',
                'handler': 'handler_to_date',
                'next_step': 'step3',
            },
            'step3': {
                'text': 'Показания погоды с {date_from} по {date_to}:\n{weather_calendar}',
                'failure_text': None,
                'handler': None,
                'next_step': None,
            },
        }
    },
    'get_images': {
        'first_step': 'step1',
        'steps': {
            'step1': {
                'text': 'Введите c какой даты хотите получить открытки',
                'failure_text': '{date_from_fail_answer}',
                'handler': 'handler_from_date',
                'next_step': 'step2',
            },
            'step2': {
                'text': 'Введите по какую дату хотите получить открытки',
                'failure_text': '{date_to_fail_answer}',
                'handler': 'handler_to_date',
                'next_step': 'step3',
            },
            'step3': {
                'text': 'Ваши открытки с погодой с {date_from} по {date_to}.',
                'failure_text': None,
                'handler': None,
                'next_step': None,
            },
        }
    },
}

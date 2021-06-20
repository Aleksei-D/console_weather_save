# -*- coding: utf-8 -*-

import datetime

from database_updater import DatabaseUpdater
from scenarios import KEY_SCENARIO, SCENARIOS
import scenario_handlers as handlers


class WeatherForecaster:
    def __init__(self, context=None):
        self.context = context or {}
        self.context['scenario'] = None

    def check_last_week(self):
        """
        Checking the weather in the BD for the last week
        :return: None
        """
        date_to = datetime.datetime.now().date()
        date_from = date_to - datetime.timedelta(days=7)
        DatabaseUpdater().check_and_update_bd(date_from=date_from, date_to=date_to)

    def display_main_menu(self):
        """
        Print main menu
        :return: None
        """
        print('1. Загрузить в базу данных погоду\n'
              '2. Вывести погоду из базы данных за период\n'
              '3. Показать карточки погоды за период\n'
              '4. Завершить работу\n'
              'Выберите действие:')

    def run(self):
        """
        Main cycle
        :return: None
        """
        self.check_last_week()
        while True:
            if self.context['scenario']:
                user_input = input()
                text_to_print = self.continue_scenario(context=self.context, user_input=user_input)
            else:
                self.display_main_menu()
                user_input = input()
                if KEY_SCENARIO.get(user_input):
                    text_to_print = self.start_scenario(context=self.context, user_input=user_input)
                elif user_input == '4':
                    print('Всего доброго!!!')
                    return False
                else:
                    text_to_print = 'Используйте указанные ключи'
            print(text_to_print)

    def start_scenario(self, context, user_input):
        """
        Start scenario
        :param context: dict
        :param user_input: Input
        :return: Text for send
        """
        context['scenario_name'] = KEY_SCENARIO[user_input]
        context['scenario'] = SCENARIOS[KEY_SCENARIO[user_input]]
        first_step = context['scenario']['first_step']
        steps = context['scenario']['steps']
        step = steps[first_step]
        text_to_print = step['text'].format(**context)
        context['step_name'] = first_step
        return text_to_print

    def continue_scenario(self, context, user_input):
        """
        Continue scenario
        :param context: dict
        :param user_input: Input
        :return: Text for send
        """
        steps = context['scenario']['steps']
        step = steps[context['step_name']]
        handler = getattr(handlers, step['handler'])
        if handler(user_input=user_input, context=context):
            next_step = steps[step['next_step']]
            text_to_print = next_step['text'].format(**context)
            if next_step['next_step']:
                context['step_name'] = step['next_step']
            else:
                context['scenario'] = None
        else:
            text_to_print = step['failure_text'].format(**context)
        return text_to_print

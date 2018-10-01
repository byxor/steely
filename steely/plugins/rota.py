'''Displays the cleaning rota'''

import random
import datetime

COMMAND = 'rota'
__author__ = 'byxor'

random.seed(420)
PEOPLE = random.shuffle(['Brandon', 'Aine', 'Matthew', 'Maria'])


def main(bot, author_id, message, thread_id, thread_type, **kwargs):
    person = get_person(week())
    next_person = get_person(week() + 1)
    message = f"Congratulations {person}, it's your turn on the cleaning rota!"
    message += f"\n{next_person} will be next... >:)"
    bot.sendMessage(message, thread_id=thread_id, thread_type=thread_type)


def week():
    d1 = datetime.date.today()
    d2 = datetime.date(2018, 10, 1)
    return (d1-d2).days//7


def get_person(week):
    return PEOPLE[week % len(PEOPLE)]

# -*- coding: utf-8 -*-
from random import choice

from dateutil.parser import parse
from pytz import timezone

from conf import ABUSES, bot


def get_abuse():
    return 'ты {1} {0}.'.format(choice(ABUSES['nouns']), choice(ABUSES['adjectives']))


def generate_redis_key(rss_url, chat_id):
    return '{}|{}'.format(rss_url, chat_id)


def get_new_entries(rss, last_update):
    response = []
    for entry in rss.entries:
        entry_updated = parse(entry.updated)
        entry_updated = entry_updated.astimezone(timezone('UTC'))
        if entry_updated > last_update:
            response.append(entry)
    return response


def send_entries(new_entries, chat_id):
    for entry in new_entries:
        bot.sendMessage(chat_id, entry.link)


def convert_rss_date_to_datetime(rss_date):
    parsed_date = parse(rss_date)
    as_utc = parsed_date.astimezone(timezone('UTC'))
    return as_utc

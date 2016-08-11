# -*- coding: utf-8 -*-
import os

import redis as rds
import telepot

redis = rds.from_url(os.environ.get('REDIS_URL', '127.0.0.1'))

TOKEN = '245698813:AAGAwMUKnAk6Zo5pcqSPOzPmSgdaqrmXJs8'

PUNEACH_CHAT_ID = '87203922'

bot = telepot.Bot(TOKEN)

bot.setWebhook('https://rocky-depths-21037.herokuapp.com/{}'.format(TOKEN))

ABUSES = {'adjectives': ('моченый', 'копченый', 'гальванический', 'метафизический', 'веселый',
                         'печальный', 'задорный', 'загадочный', 'пригожий', 'задумчивый',
                         'печеный', 'морковный', 'подозрительный', 'таинственный'),
          'nouns': ('овощ', 'пук', 'предмет', 'ботан', 'какуль', 'консервант', 'смеситель')}

ERRORS = {'rss': 'No rss found', 'token': 'Bad token', 'body': 'Invalid request body',
          'message': 'Invalid message'}

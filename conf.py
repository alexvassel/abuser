# -*- coding: utf-8 -*-

import telepot

TOKEN = '245698813:AAGAwMUKnAk6Zo5pcqSPOzPmSgdaqrmXJs8'

PUNEACH_CHAT_ID = '87203922'

bot = telepot.Bot(TOKEN)

bot.setWebhook('https://rocky-depths-21037.herokuapp.com/{}'.format(TOKEN))

ABUSES = {'adjectives': ('моченый', 'копченый', 'гальванический', 'метафизический', 'веселый',
                         'печальный', 'задорный', 'загадочный', 'пригожий', 'задумчивый',),
          'nouns': ('овощ', 'пук', 'предмет', 'ботан')}

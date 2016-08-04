# -*- coding: utf-8 -*-

from http import client
import json
from random import choice
from sys import argv

from bottle import run, post, HTTPError, request, response

from conf import bot, ABUSES, TOKEN


@post('/<bot_token>')
def index(bot_token):
    if bot_token != TOKEN:
        return HTTPError(client.FORBIDDEN, 'Bad token')
    try:
        body = json.loads(request.body.read().decode())
    except ValueError:
        return HTTPError(client.BAD_REQUEST, 'Invalid request body')

    chat_id = body['message']['chat']['id']

    resp = 'ты {1} {0}'.format(choice(ABUSES['nouns']), choice(ABUSES['adjectives']))

    bot.sendMessage(chat_id, resp, parse_mode='Markdown')

    response.content_type = 'application/json'
    return json.dumps({})

run(host='0.0.0.0', port=argv[1])

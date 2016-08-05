# -*- coding: utf-8 -*-

from http import client
import json
from sys import argv

from bottle import run, post, HTTPError, request, response

from conf import bot, TOKEN
from helpers import get_abuse


@post('/<bot_token>')
def index(bot_token):
    if bot_token != TOKEN:
        return HTTPError(client.FORBIDDEN, 'Bad token')

    try:
        body = json.loads(request.body.read().decode())
    except ValueError:
        return HTTPError(client.BAD_REQUEST, 'Invalid request body')

    chat_id = body['message']['chat']['id']

    bot.sendMessage(chat_id, get_abuse(), parse_mode='Markdown')

    response.content_type = 'application/json'
    return json.dumps({})

run(host='0.0.0.0', port=argv[1])

# -*- coding: utf-8 -*-

from http import client
import json
from sys import argv

from bottle import run, post, HTTPError, request, response
import feedparser

from conf import bot, TOKEN, ERRORS, redis
from helpers import generate_redis_key, convert_rss_date_to_datetime


@post('/<bot_token>')
def index(bot_token):
    rss = {}

    if bot_token != TOKEN:
        return HTTPError(client.FORBIDDEN, ERRORS['token'])

    try:
        body = json.loads(request.body.read().decode())
    except ValueError:
        return HTTPError(client.BAD_REQUEST, ERRORS['body'])

    try:
        message = body['message']
        rss_url = message['text']
        chat_id = message['chat']['id']
    except KeyError:
        return HTTPError(client.BAD_REQUEST, ERRORS['message'])

    parsed_rss = feedparser.parse(rss_url)

    try:
        rss['title'] = parsed_rss.feed.title
        rss['last_modified'] = convert_rss_date_to_datetime(parsed_rss.feed.modified)
    except AttributeError:
        bot.sendMessage(chat_id, ERRORS['rss'], parse_mode='Markdown')
        return

    redis_key = generate_redis_key(rss_url, chat_id)

    if redis.get(redis_key) is None:
        redis.set(redis_key, rss['last_modified'])

    bot.sendMessage(chat_id, 'RSS "{}" has been added'.format(rss['title']), parse_mode='Markdown')

    response.content_type = 'application/json'
    return json.dumps({})

run(host='0.0.0.0', port=argv[1])

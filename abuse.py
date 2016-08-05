# -*- coding: utf-8 -*-

from apscheduler.schedulers.blocking import BlockingScheduler

from conf import bot, PUNEACH_CHAT_ID
from helpers import get_abuse

scheduler = BlockingScheduler()


@scheduler.scheduled_job('cron', hour='5,12,18,13', minute=40)
def scheduled_job():
    bot.sendMessage(PUNEACH_CHAT_ID, get_abuse())

scheduler.start()

# -*- coding: utf-8 -*-

from apscheduler.schedulers.blocking import BlockingScheduler

from conf import bot, PUNEACH_CHAT_ID
from helpers import get_abuse

scheduler = BlockingScheduler()


@scheduler.scheduled_job('cron', hour='3,8,9,15', minute=25)
def scheduled_job():
    bot.sendMessage(PUNEACH_CHAT_ID, get_abuse())

scheduler.start()

# -*- coding: utf-8 -*-

from apscheduler.schedulers.blocking import BlockingScheduler

from conf import bot, PUNEACH_CHAT_ID
from helpers import get_abuse

sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=3)
def scheduled_job():
    bot.sendMessage(PUNEACH_CHAT_ID, get_abuse())

sched.start()


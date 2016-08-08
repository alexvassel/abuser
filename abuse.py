# -*- coding: utf-8 -*-

from conf import bot, PUNEACH_CHAT_ID
from helpers import get_abuse

bot.sendMessage(PUNEACH_CHAT_ID, get_abuse())

# -*- coding: utf-8 -*-
from random import choice

from conf import ABUSES


def get_abuse():
    return 'ты {1} {0}.'.format(choice(ABUSES['nouns']), choice(ABUSES['adjectives']))

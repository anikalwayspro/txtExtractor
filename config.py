#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7020914589:AAHBX4vtdnvsNY6awcrzejlTWiP2bnSd814")
    API_ID = int(os.environ.get("API_ID", "20998001"))
    API_HASH = os.environ.get("API_HASH", "08cddd6de9774509934742782266e972")
    AUTH_USERS = int(os.environ.get("AUTH_USERS", "2067727121"))

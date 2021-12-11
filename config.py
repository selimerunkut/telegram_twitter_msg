# -*- coding: utf-8 -*-
# !/usr/bin/env python3
# =============================================================================
# Created By  : Sinan Cetinkaya <sinancetinkaya35@gmail.com>
# =============================================================================
import os
import platform

APP_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
PLATFORM = platform.uname().system.lower()

TELEGRAM_USER_ID = int(os.environ.get('TELEGRAM_USER_ID'))
TELEGRAM_CHANNEL_ID = int(os.environ.get('TELEGRAM_CHANNEL_ID'))
TELEGRAM_API_ID = int(os.environ.get('TELEGRAM_API_ID'))
TELEGRAM_API_HASH = os.environ['TELEGRAM_API_HASH']
TELEGRAM_BOT_TOKEN = os.environ['TELEGRAM_BOT_TOKEN']

TWITTER_CONSUMER_KEY = os.environ['TWITTER_CONSUMER_KEY']
TWITTER_CONSUMER_SECRET = os.environ['TWITTER_CONSUMER_SECRET']
TWITTER_ACCESS_TOKEN = os.environ['TWITTER_ACCESS_TOKEN']
TWITTER_ACCESS_TOKEN_SECRET = os.environ['TWITTER_ACCESS_TOKEN_SECRET']


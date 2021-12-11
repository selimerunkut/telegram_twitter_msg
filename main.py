# -*- coding: utf-8 -*-
# !/usr/bin/env python3
# =============================================================================
# Created By  : Sinan Cetinkaya <sinancetinkaya35@gmail.com>
# =============================================================================
# Allow other computers to attach to debugpy at this IP address and port.
# python3 -m debugpy --listen 0.0.0.0:5678 --wait-for-client main.py
import asyncio
import os
from pathlib import Path
import time
import logging
from logging.handlers import TimedRotatingFileHandler
import signal
import config

LOGS_DIRECTORY = os.path.join(config.APP_DIRECTORY, 'logs')

if not os.path.exists(LOGS_DIRECTORY):
    os.makedirs(LOGS_DIRECTORY)

log_file_handler = TimedRotatingFileHandler(
    os.path.join(LOGS_DIRECTORY, f"{Path(__file__).stem}.log"),
    when="midnight",
    encoding='utf-8',
    backupCount=10
)

# noinspection PyArgumentList
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s.%(msecs)03d [%(levelname)-5.5s] %(name)s.%(funcName)s(),%(lineno)d: %(message)s',
    datefmt="%Y%m%d_%H%M%S",
    handlers=[logging.StreamHandler(), log_file_handler]
)
logging.Formatter.converter = time.localtime

LOG_LEVEL = logging.WARNING

logging.getLogger('peony').setLevel(LOG_LEVEL)
logging.getLogger('telethon').setLevel(LOG_LEVEL)

log = logging.getLogger(__name__)

if config.PLATFORM == 'windows':
    loop = asyncio.get_event_loop()
    if not loop.is_running() and not isinstance(loop, asyncio.ProactorEventLoop):
        loop = asyncio.ProactorEventLoop()
        asyncio.set_event_loop(loop)
else:
    loop = asyncio.get_event_loop()


class Main:
    def __init__(self):
        self.tasks = []
        self.shutdown = False

    async def start(self):

        from telegram import Telegram
        self.tasks.append(Telegram(loop=loop))

        for task in self.tasks:
            if hasattr(task, 'start'):
                log.debug(f"Starting: {task.__class__.__name__}")
                loop.create_task(task.start())

        while not self.shutdown:
            await asyncio.sleep(1)

        for task in self.tasks:
            if hasattr(task, 'stop'):
                log.debug(f"Stopping: {task.__class__.__name__}")
                await task.stop()
                log.debug(f"Stopped: {task.__class__.__name__}")

    def exit(self):
        self.shutdown = True


if __name__ == '__main__':
    main = Main()

    if config.PLATFORM == "linux":
        for signame in ['SIGINT', 'SIGTERM']:
            loop.add_signal_handler(sig=getattr(signal, signame), callback=main.exit)
    else:
        signal.signal(signal.SIGINT, lambda signum, frame: main.exit())

    loop.run_until_complete(main.start())

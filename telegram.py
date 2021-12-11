# -*- coding: utf-8 -*-
# !/usr/bin/env python3
# =============================================================================
# Created By  : Sinan Cetinkaya <sinancetinkaya35@gmail.com>
# =============================================================================
import asyncio
import logging
import os
from peony import PeonyClient
from peony.exceptions import HTTPBadRequest
from telethon import TelegramClient, events
from telethon.tl.types import InputPeerUser, InputPeerSelf
import config

log = logging.getLogger(__name__)


class Telegram:
    def __init__(self, loop=asyncio.get_event_loop()):
        self.loop = loop
        self.client = None
        self.twitter = None

    async def stop(self):
        if self.client:
            await self.client.disconnect()

        if self.twitter:
            await self.twitter.close()

    async def start(self):
        self.twitter = PeonyClient(
            consumer_key=config.TWITTER_CONSUMER_KEY,
            consumer_secret=config.TWITTER_CONSUMER_SECRET,
            access_token=config.TWITTER_ACCESS_TOKEN,
            access_token_secret=config.TWITTER_ACCESS_TOKEN_SECRET,
            loop=self.loop
        )

        self.client = TelegramClient(
            session='telegram',
            api_id=config.TELEGRAM_API_ID,
            api_hash=config.TELEGRAM_API_HASH,
            loop=self.loop
        )
        # useful command to get user or chat IDs from Telegram. Just type: /info
        self.client.add_event_handler(callback=self.info, event=events.NewMessage(pattern="(?i)^/info$"))

        self.client.add_event_handler(
            callback=self.on_message,
            event=events.NewMessage(
                from_users=config.TELEGRAM_USER_ID,
                incoming=True,
                chats=config.TELEGRAM_CHANNEL_ID
            )
        )

        await self.client.start(bot_token=config.TELEGRAM_BOT_TOKEN)

    async def info(self, event):
        if event.message.input_sender is None:
            await event.respond("Sender is None, 'Remain Anonymous' enabled admin?")
            return True

        if event.is_channel or event.is_group:
            # In Telegram Broadcast Channels event.message.input_sender is not User entity,
            # so there's no user permissions
            if isinstance(event.message.input_sender, (InputPeerUser, InputPeerSelf)):
                permissions = await self.client.get_permissions(
                    entity=event.message.input_chat,
                    user=event.message.input_sender
                )

                if not permissions.is_admin:
                    await event.respond("Only Channel/Group Admin can use this command")
                    return True

        await event.respond(event.chat.stringify())

    async def on_message(self, event):
        media_ids = None
        media_file = None

        try:
            # If Telegram message contains a media
            if event.message.media is not None:
                media_file = await event.message.download_media()
                media = await self.twitter.upload_media(media_file)
                media_ids = [media.media_id]
        except HTTPBadRequest:
            log.exception("")
        finally:
            if media_file:
                os.remove(media_file)

        try:
            await self.twitter.api.statuses.update.post(status=event.message.text, media_ids=media_ids)
        except:
            log.exception("")

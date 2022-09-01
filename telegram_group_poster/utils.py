from aiogram import Bot, types

from asgiref.sync import async_to_sync
from django.conf import settings
from martor.utils import markdownify


bot = Bot("settings.TELEGRAM_BOT_TOKEN", parse_mode=types.ParseMode.HTML)


@async_to_sync
async def send_message(message: str, channel_id: str = settings.TELEGRAM_CHANNEL_ID):
    await bot.send_message(channel_id, markdownify(message).replace("<p>", "").replace("</p>", ""))


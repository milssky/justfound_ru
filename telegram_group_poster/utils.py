from aiogram import Bot
from asgiref.sync import async_to_sync
from django.conf import settings

bot = Bot(settings.TELEGRAM_BOT_TOKEN)


@async_to_sync
async def send_message(message: str, channel_id: str = settings.TELEGRAM_CHANNEL_ID):
    await bot.send_message(channel_id, message)

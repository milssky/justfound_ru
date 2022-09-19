from aiogram import Bot, types

from asgiref.sync import async_to_sync
from django.conf import settings
from martor.utils import markdownify


bot = Bot(settings.TELEGRAM_BOT_TOKEN, parse_mode=types.ParseMode.HTML)


def prepare_text_to_bot(text: str) -> str:
    # TODO Очистить пост от img
    text = text.replace("<p>", "").replace("</p>", "")
    return text


@async_to_sync
async def send_message(
        message: str,
        channel_id: str = settings.TELEGRAM_CHANNEL_ID,
        cleaner: callable = prepare_text_to_bot
):
    text = cleaner(markdownify(message))
    await bot.send_message(channel_id, text)

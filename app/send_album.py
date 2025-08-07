import asyncio

from url_photo import _write_urls
from logger import logger




async def send_album(message, query, value):
    logger.info(f"id: {message.from_user.id}, username: {message.from_user.username}")
    tg_list = _write_urls(query, value)
    for media in tg_list[0]:
        await asyncio.sleep(5)
        try:
            await message.bot.send_media_group(chat_id=message.chat.id, media=media)
        except Exception as e:
            logger.warning(f"Не удалось загрузить альбом // {e}")
            await message.bot.send_message(message.chat.id, "Не удалось загрузить альбом")
            continue


    await message.bot.send_message(message.chat.id, tg_list[1])


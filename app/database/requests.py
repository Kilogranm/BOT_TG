from app.database.models import async_session
from app.database.models import User
from sqlalchemy import select

import os

async def reg_admin():
    ADMIN = int(os.getenv("ADMIN", "0").strip('"'))
    print(ADMIN)
    return ADMIN

async def set_user(message):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == message.from_user.id))

        if not user:
            # ❗ Проблема: message.date — это объект datetime, его нужно преобразовать в строку
            registration_date = message.date.strftime("%Y-%m-%d %H:%M:%S")  # <-- добавляем это


            new_user = User(
                tg_id=message.from_user.id,
                username=message.from_user.username,
                full_name=message.from_user.full_name,
                data=registration_date
            )

            session.add(new_user)

            await session.commit()


            await message.bot.send_message(reg_admin(), f"NEW USER:\
            \n{message.from_user.id}\
            \n{message.from_user.username}\
              \n{message.from_user.full_name}\
              \n{registration_date}")
        else:
            if message.from_user.username != user.username:
                session.add(User(username=message.from_user.username))



async def get_users():
    async with async_session() as session:
        result = await session.scalars(select(User))
        return result.all()
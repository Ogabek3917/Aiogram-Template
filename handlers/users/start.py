import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
<<<<<<< HEAD
from keyboards.default.neww import menu
from loader import dp
=======

from data.config import ADMINS
from loader import dp, db, bot
>>>>>>> f45e0eff8b68eca79de4e861ba72a5397c2588f5


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
<<<<<<< HEAD
    await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=menu)
=======
    name = message.from_user.full_name
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
        await message.answer(f"Xush kelibsiz! {name}")
        # Adminga xabar beramiz
        count = db.count_users()[0]
        msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
        await bot.send_message(chat_id=ADMINS[0], text=msg)

    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=f"{name} bazaga oldin qo'shilgan")
>>>>>>> f45e0eff8b68eca79de4e861ba72a5397c2588f5

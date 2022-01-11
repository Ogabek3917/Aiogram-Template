from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

confirmation_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅ Ha", callback_data="confirm"),
        InlineKeyboardButton(text="❌ Yo'q", callback_data="cancel"),
    ]]
)
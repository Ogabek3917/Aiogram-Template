from loader import dp, bot
from aiogram.types import CallbackQuery
from aiogram import types
from aiogram.dispatcher import FSMContext
from data.config import ADMINS, CHANNELS
from keyboards.default.neww import menu
from keyboards.inline.admin import confirmation_keyboard
from states.newpost import NewPost


@dp.callback_query_handler(text='confirm', state=NewPost.confirm)
async def confirm_post(call: CallbackQuery, state: FSMContext):
    # Ma'lumotlarni qayta o'qiymiz
    data = await state.get_data()
    idora = data.get('idora')
    tex = data.get('tex')
    phone = data.get('phone')
    address = data.get('address')
    hodim = data.get("hodim")
    vaqt=data.get('vaqt')
    ish_vaqt=data.get('ish_vaqt')
    maosh=data.get('maosh')
    qoshimcha=data.get('qoshimcha')
    image = data.get('image')

    msg = "📄 <b>Quyidagi ma'lumotlar qabul qilindi:</b>\n\n"
    msg += f"🏢 Idora: {idora}\n"
    msg += f"📚 Texnologiya: {tex}\n"
    msg += f"📞 Telefon: {phone}\n"
    msg += f"🌐 Hudud: {address}\n"
    msg += f"✍️ Ma'sul: {hodim}\n"
    msg += f"⏰ Murojat vaqti:{vaqt}\n"
    msg += f"⏰ Ish vaqti:{ish_vaqt}\n"
    msg += f"💸 Maosh:{maosh}\n"
    msg += f"‼️ Qo'shimcha:{qoshimcha}\n"
    await call.answer("Adminga jo'natildi", show_alert=True)
    for i in ADMINS:
        await bot.send_photo(i, image, caption=msg, reply_markup=confirmation_keyboard)
    await call.message.edit_reply_markup()
    await state.finish()


@dp.callback_query_handler(text='cancel', state=NewPost.confirm)
async def cancel_post(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("Bekor qilindi", reply_markup=menu)
    await state.finish()


@dp.callback_query_handler(text='admin_confirm')
async def confirm_post(call: CallbackQuery):
    message = await call.message.edit_reply_markup()
    await message.send_copy(chat_id=CHANNELS[0])


@dp.callback_query_handler(text='admin_cancel')
async def cancel_post(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Bekor qilindi")
from loader import dp, bot
from aiogram import types
from states.newpost import NewPost
from aiogram.dispatcher import FSMContext
from keyboards.inline.manage import confirmation_keyboard
from keyboards.default.neww import menu


@dp.message_handler(text_contains="Hodim kerak", state=None)
async def hodimkerak(message: types.Message):
    msg='Xodim topish uchun ariza berish\nHozir sizga birnecha savollar beriladi.\nHar biriga javob bering.\nOxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.'
    await message.answer(msg)
    await message.answer("🎓Idora nomini kiriting")
    await NewPost.idora.set()


@dp.message_handler(state=NewPost.idora)
async def title(message: types.Message, state: FSMContext):
    idora = message.text

    await state.update_data(
        {'idora': idora}
    )
    await message.answer("📚Texnologiya:\n\nTalab qilinadigan texnologiyalarni kiriting?\nTexnologiyalar nomlarini vergul bilan ajrating ")
    await NewPost.tex.set()


@dp.message_handler(state=NewPost.tex)
async def desc(message: types.Message, state: FSMContext):
    tex = message.text

    await state.update_data(
        {'tex': tex}
    )
    await message.answer("📞Aloqa:\n\nBog'lanish uchun raqamingizni kiriting?\nMasalan,+998 90 123 45 67")

    await NewPost.next()


@dp.message_handler(state=NewPost.phone)
async def price(message: types.Message, state: FSMContext):
    phone = message.text

    await state.update_data(
        {'phone': phone}
    )
    await message.answer("🌐Hudud:\n\nQaysi hududdansiz?\nViloyat nomi, Urganch shahar yoki Respublikani kiriting.")
    await NewPost.next()


@dp.message_handler(state=NewPost.address)
async def phone(message: types.Message, state: FSMContext):
    address = message.text

    await state.update_data(
        {'address': address}
    )
    await message.answer("✍️Ma'sul ism sharifi?")
    await NewPost.next()

@dp.message_handler(state=NewPost.hodim)
async def vaqt(message: types.Message, state: FSMContext):
    hodim = message.text

    await state.update_data(
        {'hodim': hodim}
    )
    await message.answer('⏰Murojat qilish vaqti:\n\nQaysi vaqtda murojat qilish mumin.\nMasalan:9:00 - 18:00')
    await NewPost.next()

@dp.message_handler(state=NewPost.vaqt)
async def ish(message: types.Message, state: FSMContext):
    vaqt = message.text

    await state.update_data(
        {'vaqt': vaqt}
    )
    await message.answer("⏰Ish vaqtini kiriting?")
    await NewPost.next()

@dp.message_handler(state=NewPost.ish_vaqt)
async def maosh(message: types.Message, state: FSMContext):
    ish_vaqt = message.text

    await state.update_data(
        {'ish_vaqt': ish_vaqt}
    )
    await message.answer("💸Iltimos maoshni kiriting?")
    await NewPost.next()

@dp.message_handler(state=NewPost.maosh)
async def qoshimcha(message: types.Message, state: FSMContext):
    maosh = message.text

    await state.update_data(
        {'maosh': maosh}
    )
    await message.answer("‼️Qo'shimcha ma'lumotlar?")
    await NewPost.next()


@dp.message_handler(state=NewPost.qoshimcha)
async def address(message: types.Message, state: FSMContext):
    qoshimcha = message.text

    await state.update_data(
        {'qoshimcha': qoshimcha}
    )
    await message.answer("Iltimos rasmingizni yuboring ")
    await NewPost.next()


@dp.message_handler(content_types=['photo'], state=NewPost.image)
async def image(message: types.Message, state: FSMContext):
    image = message.photo[-1].file_id

    await state.update_data(
        {'image': image}
    )
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
    await message.answer_photo(image, caption=msg, reply_markup=confirmation_keyboard)
    await NewPost.next()
    # await state.finish()
from aiogram.dispatcher.filters.state import StatesGroup, State

class NewPost(StatesGroup):
    idora = State()
    tex = State()
    phone = State()
    address = State()
    hodim = State()
    vaqt=State()
    ish_vaqt=State()
    maosh=State()
    qoshimcha=State()
    image = State()
    confirm = State()
from aiogram.dispatcher.filters.state import State, StatesGroup

class Murojaat(StatesGroup):
    ism_qabul_qilish = State()
    familya_qabul_qilish = State()
    yosh_qabul_qilish = State()
    tel_qabul_qilish = State()
    manzil_qabul_qilish = State()
    murojaat_mazmuni = State()
    tasdiqlash = State()
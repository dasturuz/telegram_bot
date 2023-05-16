from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Arizani kiritish ✍️")
        ]
    ],
    resize_keyboard=True
)

tasdiqlash = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Yuborish 👌️"),
            KeyboardButton(text="Bekor Qilish ❌")
        ]
    ],
    resize_keyboard=True
)
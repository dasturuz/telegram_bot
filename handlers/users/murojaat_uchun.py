from aiogram import types
from keyboards.default.button import button
from loader import dp


# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer(text="Assalomu alaykum. Ushbu bot orqali siz Oliy ta'lim, fan va innovatsiyalar vazirligi farg‘ona viloyati boshqarmasi uchun ariza yoki shikoyatingizni kiritishingiz mumkin.", reply_markup=button)

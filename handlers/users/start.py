from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.button import button, tasdiqlash
from loader import dp, bot
from states.holatlar import Murojaat


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alukum, {message.from_user.full_name}! \n \nUshbu bot orqali siz Oliy ta'lim, fan va innovatsiyalar vazirligi farg‘ona viloyati boshqarmasi uchun ariza yoki shikoyatingizni kiritishingiz mumkin.", reply_markup=button)

@dp.message_handler(text="Arizani kiritish ✍️")
async def bot_start(message: types.Message):
    await message.answer(text="Ismni kriting: ")
    await Murojaat.ism_qabul_qilish.set()

@dp.message_handler(state=Murojaat.ism_qabul_qilish)
async def bot_start(message: types.Message, state:FSMContext):
    ism = message.text
    await state.update_data({'ismi':ism})
    await message.answer(text="Familyani kiriting: ")
    await Murojaat.familya_qabul_qilish.set()

@dp.message_handler(state=Murojaat.familya_qabul_qilish)
async def bot_start(message: types.Message, state:FSMContext):
    fam = message.text
    await state.update_data({'familya':fam})
    await message.answer(text="Yoshingizni kiriting: ")
    await Murojaat.yosh_qabul_qilish.set()

@dp.message_handler(state=Murojaat.yosh_qabul_qilish)
async def bot_start(message: types.Message, state:FSMContext):
    yoshi = message.text
    await state.update_data({'yosh':yoshi})
    await message.answer(text="Telefon raqamni kiriting: ")
    await Murojaat.tel_qabul_qilish.set()

@dp.message_handler(state=Murojaat.tel_qabul_qilish)
async def bot_start(message: types.Message, state:FSMContext):
    teli = message.text
    await state.update_data({'tel':teli})
    await message.answer(text="Manzilingizni kiriting: ")
    await Murojaat.manzil_qabul_qilish.set()

@dp.message_handler(state=Murojaat.manzil_qabul_qilish)
async def bot_start(message: types.Message, state:FSMContext):
    manzil = message.text
    await state.update_data({'manzili':manzil})
    await message.answer(text="Murojaatingiz mazmunini kiriting: ")
    await Murojaat.murojaat_mazmuni.set()

@dp.message_handler(state=Murojaat.murojaat_mazmuni)
async def bot_start(message: types.Message, state:FSMContext):
    mazmuni = message.text
    await state.update_data({'mazmun':mazmuni})

    info = await state.get_data()
    name = info.get("ismi")
    last_name = info.get("familya")
    old = info.get("yosh")
    phone = info.get("tel")
    locat = info.get("manzili")
    murojaat = info.get("mazmun")

    send = f"Ismingiz: {name} \n" \
           f"Familyangiz: {last_name} \n" \
           f"Yoshingiz: {old} \n" \
           f"Telefon raqamingiz: {phone} \n" \
           f"Manzilingiz: {locat} \n" \
           f"Murojaatingiz mazmuni: {murojaat} \n" \

    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id, text=send, reply_markup=tasdiqlash)
    await Murojaat.tasdiqlash.set()

@dp.message_handler(state=Murojaat.tasdiqlash, text="Yuborish 👌️")
async def bot_start(message: types.Message, state:FSMContext):
    info = await state.get_data()

    name = info.get("ismi")
    last_name = info.get("familya")
    old = info.get("yosh")
    phone = info.get("tel")
    locat = info.get("manzili")
    murojaat = info.get("mazmun")

    send = f"Ismingiz: {name} \n" \
           f"Familyangiz: {last_name} \n" \
           f"Yoshingiz: {old} \n" \
           f"Telefon raqamingiz: {phone} \n" \
           f"Manzilingiz: {locat} \n" \
           f"Murojaatingiz mazmuni: {murojaat} \n" \

    channel_id = 'https://t.me/+14KXqXD60BVmZDli'
    user_id = message.from_user.id
    await bot.send_message(chat_id='@jghyrt', text=send)
    await bot.send_message(chat_id=user_id, text="Arizangiz yuborildi")
    await state.finish()


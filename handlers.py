from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from services import get_crypto_price


router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply("Введите название криптовалюты, чтобы получить курс.")

@router.message()
async def crypto_price_router(message: Message):
    currency = message.text
    try:
        price = await get_crypto_price(currency)
        await message.reply(f"Курс {currency}: {price} USD")
    except Exception as e:
        await message.reply(f"Ошибка: {str(e)}")


#@router.callback_query(F.data == "pods")
#async def
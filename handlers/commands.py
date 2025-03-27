import os

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile

from handlers.keyboards import keyboard

router = Router()

@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    img_path = os.path.join(os.path.dirname(__file__), "images", "img.png")
    img = FSInputFile(img_path)
    # await message.answer_photo(photo=img,
    #                             caption="Assalomu alekum PDP Junior botiga hush kelibsiz !")
    await message.answer("Assalomu alekum", reply_markup=keyboard)






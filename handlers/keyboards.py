from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                               keyboard=[
                                   [KeyboardButton(text="kompaniya haqida"),
                                    KeyboardButton(text="bizning mentorlar")],
                                   [KeyboardButton(text="kurslarimiz")],
                                   [KeyboardButton(text="kontaktlar /manzil"),
                                    KeyboardButton(text="til")]
                               ])

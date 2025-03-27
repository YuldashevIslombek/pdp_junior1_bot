from aiogram.types import BotCommand


async def set_bot_menu(bot):
    commands = [
        BotCommand(command="start", description="Botni boshlash!"),
        BotCommand(command="help", description="yordam!")
    ]
    await bot.set_my_commands(commands)
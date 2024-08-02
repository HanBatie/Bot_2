import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from src.Bot.hand.handlers import router
from src.Bot.hand.states.user_reg import router_reg
from src.db.engine import create_db, drop_db, async_session
from src.Bot.hand.states.new_pass_reg import router_pass


import os
from dotenv import load_dotenv

dp = Dispatcher()
dp.include_router(router)
dp.include_router(router_reg)
dp.include_router(router_pass)

async def on_startup(bot):
    run = False
    if run:
        await drop_db()
    await create_db()
async def on_shutdown(bot):
    print(':)')


async def main():
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    load_dotenv()
    bot = Bot(token=os.getenv('BOT_TOKEN'), default=DefaultBotProperties(parse_mode='HTML'))
    await dp.start_polling(bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')
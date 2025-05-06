import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config_data.config import Config, load_config
from keyboards.main_menu import set_main_menu

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s')
    logger.info("Starting bot...")

    config: Config = load_config()
    # storage = ...

    bot = Bot(token=config.tg_bot.token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    # dp = Dispatcher(storage=storage)
    dp = Dispatcher()

    some_text = 'Simple text'
    some_int = 3
    dp.workflow_data.update({'my_text': some_text, 'my_int': some_int})
    # print('From main.py dispatcher', dp.workflow_data)
    # print(dp['my_text'])
    # print(dp['my_int'])

    # await set_main_menu(bot)

    logger.info('Подключаем роутеры')

    logger.info('Подключаем миддлвари')

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())

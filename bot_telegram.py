from aiogram.utils import executor
from create_bot import dp, bot



async def on_startup(_):
    print("ბოტი ონლაინშია")






from handlers import Firstpage
Firstpage.register_handlers_Firstpage(dp)






executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
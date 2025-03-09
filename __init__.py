from aiogram import Dispatcher
from TZ1_TZ2.handlers.voice import register_voice_handler
from TZ1_TZ2.handlers.start import register_start_handler

def register_handlers(dp:Dispatcher):
    register_voice_handler(dp)
    register_start_handler(dp)


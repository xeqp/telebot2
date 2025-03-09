import tempfile
import logging
from aiogram import types, Dispatcher, Bot
from aiogram.types import Message
from aiogram import F
from TZ1_TZ2.services.openai_api import transcribe_audio, ask_assistant, text_to_speech

logging.basicConfig(level=logging.INFO)


async def voice_message_handler(message: Message, bot: Bot):
    voice = message.voice
    file = await bot.get_file(voice.file_id)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".ogg") as temp_audio:
        await bot.download_file(file.file_path, temp_audio.name)
        temp_audio_path = temp_audio.name

    text = await transcribe_audio(temp_audio_path)
    logging.info(f"Расшифрованный текст: {text}")

    user_id = str(message.from_user.id)
    text_response = await ask_assistant(user_id, text)

    logging.info(f"Ответ от ассистента: {text_response}")

    if text_response is None:
        await message.answer("Извините, не удалось получить ответ от ассистента.")
        return

    try:
        audio_path = await text_to_speech(text_response)
    except ValueError as e:
        await message.answer(f"Ошибка при преобразовании текста в речь: {e}")
        return

    audio_file = types.FSInputFile(audio_path)
    await message.answer_voice(voice=audio_file)


def register_voice_handler(dp: Dispatcher):
    dp.message.register(voice_message_handler, F.voice)

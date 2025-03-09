import openai
from gtts import gTTS

from TZ1_TZ2.settings import settings
import tempfile

openai.api_key = settings.OPENAI_API_KEY

async def transcribe_audio(file_path: str):
    try:
        with open(file_path, "rb") as audio_file:
            response = openai.Audio.transcribe(
                model="whisper-1",
                file=audio_file
            )
        return response['text']
    except Exception as e:
        print(f"Error during transcription: {e}")
        return "Error during transcription."

async def ask_assistant(user_id, text):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": text}],
            user=user_id
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        print(f"Error during OpenAI request: {e}")
        return "Sorry, I couldn't process your request."

async def text_to_speech(text_response: str):
    if not text_response:
        raise ValueError("Error: No text provided for speech generation!")
    try:
        tts = gTTS(text=text_response, lang='ru')
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
            audio_path = temp_audio.name
            tts.save(audio_path)
        return audio_path
    except Exception as e:
        print(f"Error during text-to-speech conversion: {e}")
        return None

import openai
from TZ1_TZ2.settings import settings

openai.api_key = settings.OPENAI_API_KEY

async def validate_value(value: str) -> bool:
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Validate if this is a meaningful and valid moral value: '{value}'",
            max_tokens=10
        )
        result = response.choices[0].text.strip().lower()
        return result == "true"
    except Exception as e:
        return False

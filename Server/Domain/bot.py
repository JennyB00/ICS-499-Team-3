from typing import Optional
import openai
from pydantic import BaseModel

class BotBase(BaseModel):
    username: str = "AI Bot"
    # session_id: int

class Bot(BotBase):
    openai.api_key = "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"

    def process(self, prompt: str) -> str:
        try:
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                max_tokens=100,
                temperature=1,
            )
            return response["choices"][0]["text"].replace(".", ".\n")
        except Exception as e:
            print(f"Error: {str(e)}")
            return "Error generating text"

    def generate_image(self, prompt) -> str:
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        if response["data"]:
            image_url = response['data'][0]['url']
            return image_url
        else:
            print("Error: API request failed. Please try again.")
            return "Error generating image"
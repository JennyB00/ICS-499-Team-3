import openai
from pydantic import BaseModel

openai.api_key = "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"


class Bot(BaseModel):

    def process(self, prompt: str, username: str) -> str:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=100,
            temperature=1,
            user=username
        )
        return response["choices"][0]["text"]

    def generate_image(self, prompt: str) -> str:
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        if response["data"]:
            image_url = response['data'][0]['url']
            return image_url
        else:
            raise Exception("Error generating image: API request failed")

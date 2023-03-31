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
        return response["choices"][0]["text"].replace(".", ".\n")

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

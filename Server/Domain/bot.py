import openai
from pydantic import BaseModel
import uuid


class BotBase(BaseModel):
    username: str = "AI Bot"


class Bot(BotBase):
    openai.api_key = "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"

    def __init__(self, session_id: str = str(uuid.uuid4()), *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.session_id = session_id

    def process(self, prompt: str) -> str:
        try:
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                max_tokens=100,
                temperature=1,
                prompt_context={
                    "session_id": self.session_id
                }
            )
            return response["choices"][0]["text"].replace(".", ".\n")
        except openai.error.APIError as e:
            print(f"OpenAI API returned an API Error: {e}")
            pass
        except openai.error.APIConnectionError as e:
            print(f"Failed to connect to OpenAI API: {e}")
            pass
        except openai.error.RateLimitError as e:
            print(f"OpenAI API request exceeded rate limit: {e}")
            pass

    def generate_image(self, prompt) -> str:
        try:
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
        except openai.error.APIError as e:
            print(f"OpenAI API returned an API Error: {e}")
            pass
        except openai.error.APIConnectionError as e:
            print(f"Failed to connect to OpenAI API: {e}")
            pass
        except openai.error.RateLimitError as e:
            print(f"OpenAI API request exceeded rate limit: {e}")
            pass

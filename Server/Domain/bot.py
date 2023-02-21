import openai
# from openai import openai_key
from pydantic import BaseModel

class BotBase(BaseModel):
    username: str = "AI Bot"

class BotPy(BotBase):
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
            return
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
            return

class Bot:
    openai.api_key = ""

    def __init__(self, username="AI Bot"):
        self.username = username

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
            return

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
            return

    # def chat_bot(self, username):
    #     print("Welcome to the chat bot. Type 'exit or 'quit' to end the chat.")
    #     while True:
    #         message = input(username + ": ")
    #         if message.lower() in ["exit", "quit"]:
    #             break
    #         if len(message.strip()) == 0:
    #             print("Error: Input cannot be empty.")
    #             continue
    #         response = None
    #         try:
    #             response = openai.Completion.create(
    #                 model="text-davinci-003",
    #                 prompt=message,
    #                 max_tokens=100,
    #                 temperature=1,
    #             )
    #         except Exception as e:
    #             print(f"Error: {str(e)}")
    #             continue
    #         print("Bot: {}".format(response["choices"][0]["text"].replace(".", ".\n")))

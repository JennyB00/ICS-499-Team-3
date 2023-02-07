import openai
import openai_key


class Bot:
    openai.api_key = openai_key.openai_key

    def __init__(self, username):
        self.username = username

    def receive(self, messageType, message):
        return messageType

    def process(self, message):
        return message

    def getResponse(self):
        return message

    def generate_image(self):
        prompt = input("Please describe your image: ")
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        if response["data"]:
            image_url = response['data'][0]['url']
            print("URL: " + image_url)
        else:
            print("Error: API request failed. Please try again.")

    def chat_bot(self, username):
        print("Welcome to the chat bot. Type 'exit or 'quit' to end the chat.")
        while True:
            message = input(username + ": ")
            if message.lower() in ["exit", "quit"]:
                break
            if len(message.strip()) == 0:
                print("Error: Input cannot be empty.")
                continue
            response = None
            try:
                response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=message,
                    max_tokens=100,
                    temperature=1,
                )
            except Exception as e:
                print(f"Error: {str(e)}")
                continue
            print("Bot: {}".format(response["choices"][0]["text"].replace(".", ".\n")))

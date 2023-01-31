import openai
import openai_key

openai.api_key = openai_key.openai_key


def chat_bot():
    print("Welcome to the chat bot. Type 'exit or 'quit' to end the chat.")
    while True:
        message = input("You: ")
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


if __name__ == "__main__":
    chat_bot()

import openai
import openai_key

openai.api_key = openai_key.openai_key

# prompt = "Say this is a test"
# response = openai.Completion.create(model="text-davinci-003", prompt=prompt)
# print(response["choices"][0]["text"])

while True:
    message = input("Please type anything to initiate a chat with the chat bot:")
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= message,
        max_tokens=100
    )
    print(response["choices"][0]["text"])

import os
import openai
import openai_key
openai.api_key = openai_key.openai_key

prompt = "Say this is a test"

response = openai.Completion.create(model="text-davinci-003", prompt=prompt)
#print(openai.Model.list())
print(response["choices"][0]["text"])


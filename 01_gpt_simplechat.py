import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "write content about cat"}])
print(completion.choices[0].message.content)


from openai import OpenAI
from secret import OPEN_AI_API


client = OpenAI(
    api_key=OPEN_AI_API,
)

# This one could be used in websites since give information line by line

# stream = client.chat.completions.create(
#     model='gpt-3.5-turbo',
#     messages=[
#         {'role': 'user', 'content': 'Tell me about python'},
#     ],
#     stream=True
# )

# for chunk in stream:
#     if chunk.choices[0].delta.content is not None:
#         print(chunk.choices[0].delta.content, end='')


# This one gives a role to AI allowing to get an 'Personality'
response = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        {
            'role': 'system',
            'content': 'Give technical answers, as you a professional python developer, specializing in clean architecture project'
        },
        {
            'role': 'user',
            'content': 'Can you tell me how to make a restfull api'
        },
    ],
)


print(response.choices[0].message.content)

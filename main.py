from openai import OpenAI
from secret import OPEN_AI_API


# client = OpenAI(
#     api_key=OPEN_AI_API,
# )

# stream = client.chat.completions.create(
#     model='gpt-3.5-turbo',
#     messages=[
#         {'role': 'user', 'content': 'Me fale mais sobre o fiat elba 1988'},
#     ],
#     stream=True
# )

# for chunk in stream:
#     if chunk.choices[0].delta.content is not None:
#         print(chunk.choices[0].delta.content, end='')


client = OpenAI(
    api_key=OPEN_AI_API,
)

response = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        {
            'role': 'system',
            'content': 'De respostas tecnicas sobre programacao, Se comporte como um programador python experiente, especialista em padroes de projetos e arquitetura limpa'
        },
        {
            'role': 'user',
            'content': 'Me fale como posso criar uma restfull api'
        },
    ],
)


print(response.choices[0].message.content)

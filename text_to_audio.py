from openai import OpenAI
from secret import OPEN_AI_API

client = OpenAI(
    api_key=OPEN_AI_API,
)


response = client.audio.speech.create(
    model='tts-1',
    voice='nova',
    input='',
)

response.write_to_file('meu_audio.mp3')

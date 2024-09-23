from openai import OpenAI
from secret import OPEN_AI_API

client = OpenAI(
    api_key=OPEN_AI_API,
)

audio_file = open('my_audio.mp3', 'rb')

transcription = client.audio.transcriptions.create(
    model='whisper-1',
    file=audio_file,

)

print(transcription.text)

from openai import OpenAI
from secret import OPEN_AI_API

client = OpenAI(
    api_key=OPEN_AI_API,
)

response = client.images.generate(
    model="dall-e-3",
    prompt='Person working with an Ai like tony stark and jarvis',
    size='1024x1024',
    quality='standard',
    n=1,
)

image_url = response.data[0].url
print(image_url)

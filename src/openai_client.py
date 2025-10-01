import openai
import requests
import base64

class OpenAIClient:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = api_key

    def generate_image(self, prompt, response_type):
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        image_url = response['data'][0]['url']

        if response_type == 'base64':
            image_data = self.convert_image_to_base64(image_url)
            return {
                "base64": image_data,
                "version": "0.1.0"
            }
        else:
            return {
                "image_url": image_url,
                "version": "0.1.0"
            }

    def convert_image_to_base64(self, image_url):
        response = requests.get(image_url)
        return base64.b64encode(response.content).decode('utf-8')

    def chat_completion(self, message):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message}]
        )
        return response['choices'][0]['message']['content']

def get_chat_completion(message, api_key):
    client = OpenAIClient(api_key)
    return client.chat_completion(message)

def generate_image_response(prompt, response_type, api_key):
    client = OpenAIClient(api_key)
    return client.generate_image(prompt, response_type)

import requests
import json

class GPTIntegration:
    def __init__(self, api_key):
        self.api_key = api_key
        self.endpoint = "https://api.openai.com/v1/engines/davinci-codex/completions"

    def gpt_request(self, prompt, max_tokens=100):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        data = {
            "prompt": prompt,
            "max_tokens": max_tokens,
            "n": 1,
            "stop": None,
            "temperature": 0.5
        }
        response = requests.post(self.endpoint, headers=headers, data=json.dumps(data))
        return response.json()

    def gpt_response_parser(self, response):
        if 'choices' in response and len(response['choices']) > 0:
            return response['choices'][0]['text'].strip()
        else:
            return None
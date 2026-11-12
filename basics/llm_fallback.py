from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

response = requests.post(
    url="https://openrouter.ai/api/v1/responses",
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    },
    data=json.dumps({
        "models" : ["google/gemma-4-31b-it:free", "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free"],
        "input" : "how to sustain in ai era as software developer? important 3 points enough"
    })
)
data = response.json()
output_obj = next(item for item in reversed(data['output']) if item['type'] == 'message')
msg = next(msg['text'] for msg in output_obj['content'] if msg['type'] == 'output_text')

print(msg)
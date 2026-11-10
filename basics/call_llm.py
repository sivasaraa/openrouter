from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

response = requests.post(
    url="https://openrouter.ai/api/v1/responses",
    headers={
        "Authorization": f"Bearer {api_key}"
    },
    data=json.dumps({
        "model": "liquid/lfm-3-1.7b:free",
        "input": "How to sustain in ai era? simple 3 point is enough" 
    })
)

print(json.dumps(response.json()))
from flask import current_app
import requests

def call_openai_api(prompt):
    url = current_app.config['AZURE_OPENAI_ENDPOINT']
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {current_app.config['AZURE_OPENAI_API_KEY']}"
    }
    data = {
        "prompt": prompt,
        "max_tokens": 150
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json().get('choices')[0].get('text').strip()
    else:
        raise Exception(f"OpenAI API call failed with status code {response.status_code}: {response.text}")
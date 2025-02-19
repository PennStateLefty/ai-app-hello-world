from flask import current_app
#from azure.ai.openai import OpenAIClient
from openai import AzureOpenAI
from azure.core.credentials import AzureKeyCredential

class AzureOpenAIService:
    def __init__(self, endpoint, api_key):
        self.client = AzureOpenAI(
            azure_endpoint=endpoint,
            api_version="2024-05-01-preview",
            api_key=api_key
        )

    def call_openai(self, prompt):
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful assistant who loves Shakespeare."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            raise Exception(f"OpenAI API call failed: {e}")

    @staticmethod
    def init_openai_service(endpoint, api_key):
        return AzureOpenAIService(endpoint, api_key)
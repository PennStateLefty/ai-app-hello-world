from flask import Blueprint, request, jsonify, current_app
from app.services import azure_openai
from app.services.azure_openai import AzureOpenAIService

bp = Blueprint('main', __name__)

@bp.route('/process', methods=['POST'])
def process_text():
    data = request.json
    text_input = data.get('text')

    if not text_input:
        return jsonify({'error': 'No text input provided'}), 400

    # Store input in CosmosDB
    current_app.cosmosdb_service.store_input({'id': 'some_unique_id', 'text': text_input})

    # Call Azure OpenAI assistant API
    openai_service = AzureOpenAIService(
        endpoint=current_app.config['AZURE_OPENAI_ENDPOINT'],
        api_key=current_app.config['AZURE_OPENAI_API_KEY']
    )
    response = openai_service.call_openai(text_input)

    # Store result in Azure Cache for Redis
    current_app.redis_cache_service.store_result(text_input, response)

    return jsonify({'response': response}), 200
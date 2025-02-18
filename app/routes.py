from flask import Blueprint, request, jsonify
from app.services import cosmosdb, azure_openai, redis_cache

bp = Blueprint('main', __name__)

@bp.route('/process', methods=['POST'])
def process_text():
    data = request.json
    text_input = data.get('text')

    if not text_input:
        return jsonify({'error': 'No text input provided'}), 400

    # Store input in CosmosDB
    cosmosdb.store_input(text_input)

    # Call Azure OpenAI assistant API
    response = azure_openai.call_openai(text_input)

    # Store result in Azure Cache for Redis
    redis_cache.store_result(text_input, response)

    return jsonify({'response': response}), 200
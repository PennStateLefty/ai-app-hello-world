# Flask Application with Azure Integration

This project is a Flask application that takes text input from users, stores it in Azure CosmosDB, interacts with the Azure OpenAI assistant API, and caches the results in Azure Cache for Redis.

## Project Structure

```
flask-app
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   └── services
│       ├── azure_openai.py
│       ├── cosmosdb.py
│       └── redis_cache.py
├── requirements.txt
├── config.py
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd flask-app
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```
   pip install -r requirements.txt
   ```

4. **Configure your application:**
   - Update the `config.py` file with your Azure CosmosDB connection string, Azure OpenAI API key, and Azure Cache for Redis connection details.

5. **Run the application:**
   ```
   flask run
   ```

## Usage

- Send a POST request to the `/process` endpoint with a JSON body containing the text input:
  ```json
  {
      "text": "Your input text here"
  }
  ```

- The application will store the input in CosmosDB, call the Azure OpenAI assistant API, and return the response.

## Dependencies

- Flask
- Azure SDK for Python
- Redis
- Any other necessary libraries listed in `requirements.txt`.

## License

This project is licensed under the MIT License.
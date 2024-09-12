# Free Translate API (Python Version)

Welcome to the Python version of the Free Translate API! This API allows you to perform translations between different languages without any limits. This project is inspired by the original version written in Go by [Ismal Zikri](https://github.com/ismalzikri/free-translate-api), but ported to Python using FastAPI and deep-translator.

## Table of Contents

- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Usage](#usage)
- [Supported Languages](#supported-languages)
- [API Endpoints](#api-endpoints)
- [Example Requests](#example-requests)
  - [Command Line (cURL)](#command-line-curl)
  - [PowerShell](#powershell)
  - [Python Example](#python-example)
  - [JavaScript Example](#javascript-example)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Installation

To use this Python version of the Free Translate API, you'll need [Python](https://www.python.org/downloads/) installed on your system. After that, follow these steps to get started:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repo/free-translate-api-python.git
   cd free-translate-api-python
   ```

2. Install dependencies using `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

Start the API server:

```bash
uvicorn main:app --reload
```

The API server will start running on `http://localhost:8000`.

You can now send translation requests to the API using HTTP POST requests. The endpoint for translation is `/translate`. Here's an example using curl:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"text": "Hello", "to": "es"}' http://localhost:8000/translate
```

## Supported Languages

This Python-based Free Translate API supports translation between a wide range of languages using the `deep-translator` library. You can use common language codes like `"en"` for English, `"es"` for Spanish, `"fr"` for French, and more.

For a full list of supported languages, you can refer to [this documentation](https://github.com/nidhaloff/deep-translator#supported-languages).

## API Endpoints

### `POST /translate`

Translates the provided text to the specified target language. The request body should be a JSON object with the following structure:

```json
{
  "text": "Hello",
  "to": "es"
}
```

The response will contain the translated text:

```json
{
  "translatedText": "Hola",
  "status": true,
  "message": ""
}
```

## Example Requests

### Command Line (cURL)

```bash
curl -X POST -H "Content-Type: application/json" -d '{"text": "Hello", "to": "es"}' http://localhost:8000/translate
```

### PowerShell

```powershell
Invoke-RestMethod -Method Post -Uri "http://localhost:8000/translate" -Headers @{"Content-Type"="application/json"} -Body '{"text": "Hello", "to": "es"}'
```

### Python Example

```python
import requests

url = "http://localhost:8000/translate"
data = {
    "text": "Hello",
    "to": "es"
}

response = requests.post(url, json=data)
print(response.json())
```

### JavaScript Example

```javascript
fetch('http://localhost:8000/translate', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    text: 'Hello',
    to: 'es',
  }),
})
  .then((response) => response.json())
  .then((data) => console.log(data))
```

## Contributing

Contributions to the Free Translate API are always welcome! If you find any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

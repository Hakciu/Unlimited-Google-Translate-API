# Free Translate API (Python Version)

Welcome to the Python version of the Free Translate API! This API allows you to perform translations between different languages without any limits. This project is inspired by the original version written in Go by [Ismal Zikri](https://github.com/ismalzikri/free-translate-api), but ported to Python using FastAPI and deep-translator. The API automatically detects the language of the provided text and translates it to the target language.

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
   git clone https://github.com/Hakciu/Unlimited-Google-Translate-API.git
   cd Unlimited-Google-Translate-API
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

This Python-based Free Translate API supports a wide range of languages using the `deep-translator` library. You can automatically detect the input language and specify the target language. Below is the list of supported languages and their codes:

```
AFRIKAANS = "af"
ALBANIAN = "sq"
AMHARIC = "am"
ARABIC = "ar"
ARMENIAN = "hy"
AZERBAIJANI = "az"
BASQUE = "eu"
BELARUSIAN = "be"
BENGALI = "bn"
BOSNIAN = "bs"
BULGARIAN = "bg"
CATALAN = "ca"
CEBUANO = "ceb"
CHINESE_SIMPLIFIED = "zh-CN"
CHINESE_TRADITIONAL = "zh-TW"
CORSICAN = "co"
CROATIAN = "hr"
CZECH = "cs"
DANISH = "da"
DUTCH = "nl"
ENGLISH = "en"
ESPERANTO = "eo"
ESTONIAN = "et"
FINNISH = "fi"
FRENCH = "fr"
FRISIAN = "fy"
GALICIAN = "gl"
GEORGIAN = "ka"
GERMAN = "de"
GREEK = "el"
GUJARATI = "gu"
HAITIAN_CREOLE = "ht"
HAUSA = "ha"
HAWAIIAN = "haw"
HEBREW = "he"
HINDI = "hi"
HMONG = "hmn"
HUNGARIAN = "hu"
ICELANDIC = "is"
IGBO = "ig"
INDONESIAN = "id"
IRISH = "ga"
ITALIAN = "it"
JAPANESE = "ja"
JAVANESE = "jv"
KANNADA = "kn"
KAZAKH = "kk"
KHMER = "km"
KINYARWANDA = "rw"
KOREAN = "ko"
KURDISH = "ku"
KYRGYZ = "ky"
LAO = "lo"
LATIN = "la"
LATVIAN = "lv"
LITHUANIAN = "lt"
LUXEMBOURGISH = "lb"
MACEDONIAN = "mk"
MALAGASY = "mg"
MALAY = "ms"
MALAYALAM = "ml"
MALTESE = "mt"
MAORI = "mi"
MARATHI = "mr"
MONGOLIAN = "mn"
MYANMAR = "my"
NEPALI = "ne"
NORWEGIAN = "no"
NYANJA = "ny"
ODIA = "or"
PASHTO = "ps"
PERSIAN = "fa"
POLISH = "pl"
PORTUGUESE = "pt"
PUNJABI = "pa"
ROMANIAN = "ro"
RUSSIAN = "ru"
SAMOAN = "sm"
SCOTS_GAELIC = "gd"
SERBIAN = "sr"
SESOTHO = "st"
SHONA = "sn"
SINDHI = "sd"
SINHALA = "si"
SLOVAK = "sk"
SLOVENIAN = "sl"
SOMALI = "so"
SPANISH = "es"
SUNDANESE = "su"
SWAHILI = "sw"
SWEDISH = "sv"
TAGALOG = "tl"
TAJIK = "tg"
TAMIL = "ta"
TELUGU = "te"
THAI = "th"
TURKISH = "tr"
UKRAINIAN = "uk"
URDU = "ur"
UZBEK = "uz"
VIETNAMESE = "vi"
WELSH = "cy"
XHOSA = "xh"
YIDDISH = "yi"
YORUBA = "yo"
ZULU = "zu"
```

## API Endpoints

### `POST /translate`

Translates the provided text to the specified target language. The request body should be a JSON object with the following structure:

```json
{
  "text": "Hello",
  "to": "es"
}
```

The API automatically detects the language of the provided text and returns the translated text in the response:

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

### JavaScript Example (using async/await)

```javascript
async function translateText() {
  const response = await fetch('http://localhost:8000/translate', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      text: 'Hello',
      to: 'es',
    }),
  })
  const data = await response.json()
  console.log(data)
}

translateText()
```

## Contributing

This project was created because I needed a solution to translate product descriptions into multiple languages for my work. Contributions to the Free Translate API are always welcome! If you find any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

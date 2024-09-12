from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from deep_translator import GoogleTranslator
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import logging

app = FastAPI()

# Konfiguracja CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Pozwala na wszystkie źródła
    allow_credentials=True,
    allow_methods=["*"],  # Pozwala na wszystkie metody HTTP
    allow_headers=["*"],  # Pozwala na wszystkie nagłówki
)

# Model danych wejściowych
class TranslateRequest(BaseModel):
    text: str
    to: str

# Model danych wyjściowych
class TranslateResponse(BaseModel):
    translatedText: str = None
    status: bool
    message: str

# Funkcja pomocnicza do wysyłania odpowiedzi w przypadku błędu
def send_error_response(message: str, status_code: int):
    return TranslateResponse(status=False, message=message)

@app.post("/translate", response_model=TranslateResponse)
async def translate_text(request: Request):
    try:
        body = await request.json()  # Pobierz dane JSON z requesta
        request_data = TranslateRequest(**body)

        # Użycie deep_translator do tłumaczenia
        translated_text = GoogleTranslator(source='auto', target=request_data.to).translate(request_data.text)

        response = TranslateResponse(
            translatedText=translated_text,
            status=True,
            message=""
        )
        return response  # Usuwamy dodatkowy kod statusu

    except Exception as e:
        logging.error(f"Error during translation: {e}")
        return send_error_response("Translation failed", 500)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

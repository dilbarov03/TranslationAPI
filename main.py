import translators as ts
from fastapi import FastAPI
from models import TranslateModel, TranslateResponse, LanguageResponse
from translate import language_codes

app = FastAPI()


@app.post("/translate", response_model=TranslateResponse)
def translate(translate: TranslateModel):
    """
    Translate text from one language to another.
    """
    from_language = translate.from_lang or "auto"
    result = ts.translate_text(translate.text, from_language=from_language, to_language=translate.to_lang, translator="google")
    return {"result": result}


@app.get("/languages", response_model=LanguageResponse)
def get_languages():
    """
    Get a list of supported languages.
    """
    return language_codes

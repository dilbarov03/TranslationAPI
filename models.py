from pydantic import BaseModel

class TranslateModel(BaseModel):
    from_lang: str = None
    to_lang: str
    text: str
    
    
class TranslateResponse(BaseModel):
    result: str
    

class LanguageResponse(BaseModel):
    language_name: str
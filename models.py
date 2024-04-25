from pydantic import BaseModel

class TranslateModel(BaseModel):
    from_lang: str = None
    to_lang: str
    text: str
    
    
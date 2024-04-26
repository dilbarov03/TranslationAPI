
# Fast Translate API Documentation

Welcome to the Fast Translate API! This API allows you to translate text from one language to another using various language pairs supported by the underlying translation service.

## Endpoints

### Translate Text
Translate text from one language to another.

#### Endpoint

`POST /translate` 

#### Request Body
-   `text` (string, required): The text to be translated.
-   `from_lang` (string, optional): The language code of the source language. If not provided, the language will be detected automatically.
-   `to_lang` (string, required): The language code of the target language.

#### Response
-   `result` (string): The translated text.
#### Example
`POST /translate`

    {
      "text": "Hello, how are you?",
      "from_lang": "en",
      "to_lang": "fr"
    }

 

#### Response Example

`{
  "result": "Bonjour, comment vas-tu ?"
}` 

### Supported Languages

Get a list of supported languages and their corresponding language codes.

#### Endpoint
`GET /languages` 
#### Response
-   A dictionary containing language codes and their corresponding language names.
#### Example
`GET /languages` 

#### Response Example
`{
  "Afrikaans": "af",
  "Albanian": "sq",
  "Amharic": "am",
  ...
}`

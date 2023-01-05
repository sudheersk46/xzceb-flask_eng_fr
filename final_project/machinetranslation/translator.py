"""
#Programme to Translate text with flask
"""

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2022-12-29',
    authenticator=authenticator
)

language_translator.set_service_url(url)

language_translator.set_disable_ssl_verification(True)

languages = language_translator.list_languages().get_result()
#print(json.dumps(languages, indent=2))

def english_to_french(englishtext):
    """
    Function to translate englsh to french
    """
    translation = language_translator.translate(
    text=englishtext,
    model_id='en-fr').get_result()
#    print(json.dumps(translation, indent=2, ensure_ascii=False))
    return translation.get(‘translations’)[0].get(‘translation’)

def french_to_english(frenchtext):
    """
    Function to translate french to english
    """
    translation = language_translator.translate(
    text=englishtext,
    model_id='fr-en').get_result()
#    print(json.dumps(translation, indent=2, ensure_ascii=False))
    return translation.get(‘translations’)[0].get(‘translation’)

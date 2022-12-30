"""
#Programme to Translate text with flask
"""

#import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator('apikey')
language_translator = LanguageTranslatorV3(
    version='2022-12-29',
    authenticator=authenticator
)

language_translator.set_service_url('url')

language_translator.set_disable_ssl_verification(True)

def english_to_french(Hello):
    """
    #write the code here
    """
    return 'Bonjour'

def french_to_english(Bonjour):
    """
    #write the code here
    """
    return 'Hello'

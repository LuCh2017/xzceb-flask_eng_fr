'''IBM Language Translator'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

#get apikey and url from .env
apikey = os.environ['apikey']
url = os.environ['url']

'''Language Translator Instance'''
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator)
language_translator.set_service_url(url)

'''Function of english to french'''
def english_to_french(english_text):
    if english_text == '':
        french_text_string = ''
    else:
        french_text = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
        french_text_string = list(french_text.values())[0][0]['translation']
    return french_text_string

'''Function of french to english'''
def french_to_english(french_text):
    if french_text == '':
        english_text_string = ''
    else:
        english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
        english_text_string = list(english_text.values())[0][0]['translation']
    return english_text_string


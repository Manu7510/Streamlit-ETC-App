# -*- coding: utf-8 -*-
"""
Created on Thu May  6 12:55:41 2021

@author: Manu
"""

# Load the essentials libraries

import easyocr
from gtts import gTTS
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

#translate
apikey='AxS5LivIZH5-D41KiOho6ePWUkYCiVbGlCh0FvlOIlwW'
url='https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/7c2fc8f3-8504-4fbd-8126-bf46004f8032'

#setup service
authenticator=IAMAuthenticator(apikey)
lt=LanguageTranslatorV3(version='2018-05-01',authenticator=authenticator)
lt.set_service_url(url)

# This is a function to extract text from the bounding boxes
def display_text(bounds):
    text = []
    for x in bounds:
        t = x[1]
        text.append(t)
    text = ' '.join(text)
    return text

# This function translates text from source to destination language
def translate_text(area):
    lng=lt.identify(area).get_result()

    var=lng['languages'][0]['language']

    return var

# This function translates text from source to destination language
def ex_text(texts,lang):
    trans=lt.translate(texts, model_id=lang).get_result()

    var1=trans['translations'][0]['translation']

    return var1

# This function extract text from image
def extractfrom_image(img):

    eng_reader = easyocr.Reader(['en','hi'])
    detected_text = eng_reader.readtext(img)
    texts = display_text(detected_text)

    return texts

# This function converts text to audio and save it
def textto_audio(texts,lang,type):

    out_path = "./out/trans_"+type+".mp3"
    ta_tts = gTTS(texts,lang=f'{lang}')
    ta_tts.save(out_path)

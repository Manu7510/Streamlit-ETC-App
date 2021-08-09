# -*- coding: utf-8 -*-
"""
Created on Thu May  6 12:55:41 2021

@author: Manu
"""

# Load the esseentials libraries
import utils

# This is a function to translate simple text
def simple_translate(area):

    #Call the translate function
    translated_text = utils.translate_text(area)

    return translated_text

def extract_translate(texts,lang):

    #Call the translate function
    trans_text = utils.ex_text(texts,lang)

    return trans_text

# This is a function to extract text from image and save as audio
def extractfromImage_saveaudio(img,lang,type):

    helper = {'English':'en','Hindi':'hi','Bengali':'bn','Gujarati':'gu','Kannada':'kn','Malayalam':'ml','Marathi':'mr','Odia (Oriya)':'or','Punjabi':'pa','Tamil':'ta','Telugu':'te'}
    texts = utils.extractfrom_image(img)
    language = helper[lang]
    utils.textto_audio(texts,language,type)

    return texts

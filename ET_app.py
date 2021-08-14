# -*- coding: utf-8 -*-
"""
Created on Thu May  6 12:55:41 2021

@author: Manu
"""

# Load the essentials libraries
from PIL import Image
import numpy as np
import process as pp
import streamlit as st
import utils



col1,col2,col6 = st.columns(3)
nav=st.sidebar.radio("Navigation bar", ["Home","ETC","Lang_identify"])

helper = {'English':'en','Hindi':'hi','Bengali':'bn','Gujarati':'gu','Kannada':'kn','Malayalam':'ml','Marathi':'mr','Odia (Oriya)':'or','Punjabi':'pa','Tamil':'ta','Telugu':'te'}
help = ['','en-hi','en-ml','hi-en','hi-ml']


st.set_option('deprecation.showfileUploaderEncoding',False)

if nav == "Lang_identify" :

        st.title("Enter Text")
        area = st.text_area("Identify any language at any time ")

        if st.button("Identify!"):

            answer = pp.simple_translate(area)

            st.write(answer)
            st.balloons()

elif nav == "ETC" :
    st.sidebar.title('Language Selection Menu')
    src = st.sidebar.selectbox("Source Language:",['English','Hindi','Bengali','Gujarati','Kannada','Malayalam','Marathi','Odia (Oriya)','Punjabi','Tamil','Telugu'])
    lang = st.sidebar.selectbox("SELECT OPTION",help)
    destination = st.sidebar.selectbox("Audio target Language",['English','Hindi','Bengali','Gujarati','Kannada','Malayalam','Marathi','Odia (Oriya)','Punjabi','Tamil','Telugu'])
    dst = helper[destination]

    #src = helper[source]

    st.title('ETC APP')
    st.subheader('Optical Character Recognition with Voice output')
    st.text('Select source Language from the Sidebar.')

    image_file = st.file_uploader("Upload Image",type=['jpg','png','jpeg','JPG'])
    if st.button("Convert"):

        if image_file is not None:
            img = Image.open(image_file)
            img = np.array(img)
            st.subheader('Image you Uploaded...')
            st.image(image_file,width=450)

            with st.spinner('Extracting Text from given Image'):
                texts = pp.extractfromImage_saveaudio(img,src,"source")
                st.success("Extracted Text")
                st.write(texts)
                st.audio('./out/trans_source.mp3',format='audio/mp3')

                with st.spinner('Translating Text...'):

                    result = pp.extract_translate(texts,lang)
                    st.success("Translated Text")
                    st.write(result)

                    st.write('')

                with st.spinner('Generating Audio ...'):

                    utils.textto_audio(result,dst,"destination")

                    st.success('Generated Audio :sunglasses:')
                    st.audio('./out/trans_destination.mp3',format='audio/mp3')

                st.balloons()


        else:
            st.error('Image not found! Please Upload an Image.')

if nav == "Home" :

    with col2:

        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")

        st.write("")
        st.write("")
        st.write("")
        st.write("")

        st.image("./logo5.PNG")

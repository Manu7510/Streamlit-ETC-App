# Signboard Translation from Vernacular Languages
We live in a society where we speak with individuals and data framesworks with differing media. 
Large volume of data is represented in natural scenes.
Signs are all around in our lives. A sign is an article that proposes the nearness of actuality. 
It can be a shown structure bearing letters or symbols, used to recognize something or publicize a business. 
It can be a posted notification bearing a warning, safety advisory or command etc. 
They make our lives simpler when we can read and follow them, but they posture issues or much threat when we are most certainly not.
For instance, a traveler won't have the capacity to understand a sign in local language that indcates notices or risks. 
This project mainly concentrates on recognzing text on signs.
Signboard translator is a web app built in Streamlit, that uploads the signboard image , extracts the text from image, translates it to the desired language and converts it to audio.
Here easyocr is used to extract the image text , IBM Watson API to translate it and gTTS for audio conversion.
IBM Watson also provides language identification feature that is also added here.

## Features
* Extract - Translate - Convert
* Identify any language 

**Provided an ouput in Out folder, where the signboard text was Reserved Parking.**
**Two files provided in that folder , one with audio of extracted text an other with audio of translated text.**

# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 22:20:30 2018

@author: Kartikay
"""

# Import the required module for text 
# to speech conversion
from gtts import gTTS
from playsound import playsound
 
# This module is imported so that we can 
# play the converted audio
import os
 
# The text that you want to convert to audio
mytext =input("enter the text ")
 
# Language in which you want to convert
language = 'en'
 
# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)
 
# Saving the converted audio in a mp3 file named
# welcome 
myobj.save("sid1.mp3")
 
# Playing the converted file
playsound('sid1.mp3')
#os.system("mpg321 welcome123.mp3")
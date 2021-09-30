from typing import Text
from gtts import gTTS
import os
text = input('Enter your statement: ')
lng = 'en'
mobj = gTTS(text = text, lang = lng, slow = False)
mobj.save(r'C:\Users\kriss\desktop\Test.mp3')
os.system(r'C:\Users\kriss\desktop\Test.mp3')
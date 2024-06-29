from playsound import playsound
from gtts import gTTS
import os
import cv2
import time
print ("enter text")
x=input()
print(x)
time.sleep(1)
print('you said{}'.format(x))
if x=='how many days in week' or x=='days':
    y=7
    m1=gTTS("text=y,lang=tn,slow=false")
    m1.save("voice.mp3")
    playsound("voice.mp3")
    os.reomove("voice.mp3")

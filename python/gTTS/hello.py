from gtts import gTTS
from io import BytesIO
from playsound import playsound
from say import *

file = 'kongyiji.opus'
text = """
打发时间随便问问
"""
tts = gTTS(text, lang='zh-CN')
tts.save(file)

# playsound(file)


# say(text)

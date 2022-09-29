from gtts import gTTS
from io import BytesIO
from playsound import playsound
from say import *

file = 'kongyiji.opus'
text = """ say命令的用法. 进入终端后,输入man sa  可以查看say详细的语法
"""
tts = gTTS(text, lang='zh-CN')
tts.save(file)

playsound(file)


# say(text)

from gtts import gTTS
from io import BytesIO
from playsound import playsound
from say import *

file = 'kongyiji.mp3'
text = """
1. 下载安装ES对应Plugin Release版本
安装方式：

方式一

a. 下载对应的release安装包，最新release包可从baidu盘下载（链接:https://pan.baidu.com/s/1mFPNJXgiTPzZeqEjH_zifw 密码:i0o7）


"""
# tts = gTTS(text, lang='zh-CN')
# tts.save(file)

# playsound(file)


say(text)

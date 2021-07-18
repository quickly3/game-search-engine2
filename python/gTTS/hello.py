from gtts import gTTS
from io import BytesIO
from playsound import playsound
from say import *

file = 'kongyiji.opus'
text = """
InfoQ 热门话题（2021-07-14）
1. 技术债管理的七大挑战
2. 闲鱼的统一跨端 API 方案 —— Uni API
3. ECUG Meetup 第 1 期丨2021 音视频技术最佳实践
4. 唯品会亿级数据服务平台落地实践
5. 云原生可观测建设要点与案例分析
6. 持续集成和交付流水线的反模式
7. 靠系统bug骗取超千万美元，微软一软件工程师锒铛入狱
8. 怎样编写人们容易阅读的代码？
9. 【技术实践】基于Cglib动态代理，实现Spring的AOP核心功能！
10. 专访“舆情”从业技术人：抓住中台契机，推动了一场技术变革
11. B站崩了：事情不大，影响不小
12. FAST代表的是星辰大海，腾讯做这件事并不是为了经济收益
13. 程序员 ：我怀疑你在偷窥我的生活
14. 三位深度学习先驱联合发文：深度学习的挑战与未来
"""
tts = gTTS(text, lang='zh-CN')
tts.save(file)

# playsound(file)


# say(text)

import requests
import json
import re
import time
import random

from Qzone_auto_twitter import QzoneSpider as autoTwitter
from dotenv import load_dotenv
import os

load_dotenv(verbose=True, override=True, encoding='utf-8')
appid = os.getenv('appid')
appsecret = os.getenv('appsecret')


def getWindSpeed(city):  # 获取风速
    math = random.randint(0,10)
    cletter = ''
    if math == 0:
        cletter = 'a'
    elif math == 1:
        cletter = 'b'
    elif math == 2:
        cletter = 'c'
    elif math == 3:
        cletter = 'd'
    elif math == 4:
        cletter = 'e'
    elif math == 5:
        cletter = 'f'
    elif math == 6:
        cletter = 'g'
    elif math == 7:
        cletter = 'h'
    elif math == 8 :
        cletter = 'i'
    elif math == 9:
        cletter = 'k'
    elif math == 10:
        cletter = 'l'
       
        
    apiUrl = "https://v1.hitokoto.cn/?encode=text&c" % (cletter)
    print(apiUrl)
    try:
        data = requests.get(apiUrl)
        print("获取一言数据成功")
    except:
        print("获取一言数据失败")
    try:
        print(data.text)
        decode = json.loads(data.text)
        print("解析风力成功")
        print("风力：" + decode['win_speed'])
        return decode['win_speed']
    except:
        print("解析风力数据失败")


if __name__ == '__main__':
    attempts = 0
    success = False
    while attempts < 3 and not success:
        try:
            print("城市：" + windCity)
            msg = ""
            for i in range(int(re.search(r"(\d)级", getWindSpeed(windCity)).group(1))):
                msg = msg + "呼呼"
            msg = msg + "\n\n" + requests.get("https://v1.hitokoto.cn/?encode=text").text
            print("今日句子：\n" + msg)
            # Qzone(msg)
            autoTwitter().pMsg(msg = msg)
            success = True
            print('发送成功')
        except:
            print("出现错误正在重试...")
            attempts += 1
            if attempts == 3:
                print("超过重试次数 结束程序")
                break

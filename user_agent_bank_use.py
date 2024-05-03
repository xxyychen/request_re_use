# -*- coding = utf-8 -*-
# @Time : 2024/4/21 21:38
# @Author : 鬼鬼
# @File : user_agent_bank_use.py
# @Software: PyCharm


if __name__ == "__main__":

    # 借助 库 ===========================
    from fake_useragent import UserAgent
    ua = UserAgent()    # 需要连接他们的服务器，然后得到data

    for i in range(8):
        headers = {'User-Agent': ua.random} #不太稳定，稳定的是自己建一个ua池
        print(headers)


    # 自己搭建ua池 ===========================
    # ua_s = ['ua_1', 'ua_2', 'ua_3', 'ua_4', 'ua_5', 'ua_6', 'ua_7', 'ua_8', 'ua_9', 'ua_10']
    #
    # import random
    # for i in range(8):
    #     headers = { 'User-Agent':random.choice(ua_s) }
    #     print(headers)

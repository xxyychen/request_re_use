# -*- coding = utf-8 -*-
# @Time : 2024/4/20 20:50
# @Author : 鬼鬼
# @File : request_method_2_internal.py
# @Software: PyCharm

import requests

from request_mathod import header



if __name__ == "__main__":

    url = "https://xxx.com/"
    req = requests.get(url,headers=header)

    print(req.status_code)

    print(req.text)
    # print(req.json())

    #  ============================================
    # print(res.encoding)
    # res.encoding = 'utf-8'  # 设定编码格式


    # ============================================
    # print(res.content)  # bytes   decode
    # print(res.content.decode())  # 默认utf-8
    # print(res.content.decode('utf-8'))


    # ============================================
    # print(res.request.headers)  # 请求头
    # print(res.headers)          # 响应头
    # print(res.url)
    # print(res.cookies)


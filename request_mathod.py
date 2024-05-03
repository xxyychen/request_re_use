# -*- coding = utf-8 -*-
# @Time : 2024/4/17 15:48
# @Author : 鬼鬼
# @File : request_mathod.py
# @Software: PyCharm

import requests

# 伪装请求头
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}


def get_params(search, page, number):

    print("        from urllib.parse import urlencode        ")

    # configs
    """
        :param search:
        :param page:
        :param number:
        :return:
    """
    # ==============================================
    # ============  url-参数params-拼接  ============
    # ==============================================
    url = 'https://image.baidu.com/search/acjson'
    params = {
        "ct": "201326592",
        "queryWord": search,
        "latest": "",
        'start': page,
        "pn": str(60 * page),
        "rn": number,
        "1617626956685": ""
    }
    # json 对象格式为dict
    # result = requests.get(url, headers=header, params=params, timeout=5).json()

    return url, params


def param_url_encode_unquote():


    print("----- url-encode编码 -----")

    from urllib.parse import urlencode

    params = {
        "pagination_str": {"offset": ""}
    }
    params = urlencode(params, encoding='GB2312')  # encoding='gbk'   encoding='utf-8'  都一样
    print(params)


    url = 'https://pic.sogou.com/napi/pc/searchList?' + urlencode(params)
    # print(url)  #  # https://pic.sogou.com/napi/pc/searchList?mode=1&start=3&xml_len=48&query=%E7%8C%AB


    print("----- decode解码 -----")
    import urllib.request
    ss = '%7B%22offset%22%3A%22%22%7D'

    u = urllib.request.unquote(ss)
    print(u)





def request_session():

    A = requests.session()
    A.headers = header
    # 登录花瓣网 案例

    # 先前端  查看bootstrap代码的样子，分析  表单
    # 如： "method":post  "action":session   input
    # 页面不变 就是200   页面跳转  就是重定向302

    # 首页源码---------------------------------
    # ===============  A.get  ===============
    base_url = "https://huaban.com/"
    res_b = A.get(base_url)
    print("首页源码")
    print(res_b.text)

    # ===============  A.post  ===============
    login_url = "https://api.huaban.com/auth/"
    data = {
        'email': '13216761024',
        'password': '133838632306.'
    }
    res_l = A.post(login_url, data=data)  # 登陆后自动记录cookie
    print("登录：")
    print(res_l.text)

    # ===============  A.get  ===============
    user_url = "https://huaban.com/user/islzkckhmz"
    res = A.get(user_url)

    # ===============  re.findall  ===============
    import re
    sr = re.findall('<img class="hb-image" alt="(.*?)" title=', res.text)[1]
    print(sr)


def write_html():

    print("----- wb -----")
    # with open("baidu.html","wb") as f:
    #     f.write(res.content)






if __name__ == "__main__":

    pass



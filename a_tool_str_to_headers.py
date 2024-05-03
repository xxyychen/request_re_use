# -*- coding = utf-8 -*-
# @Time : 2024/4/25 19:53
# @Author : 鬼鬼
# @File : a_tool_str_to_headers.py
# @Software: PyCharm

import re


def extract_headers(headers):
    headers = headers.replace('\\n', '\n')
    sorted_headers = {}
    matches = re.findall(r'(.*):\s(.*)', headers)
    for match in matches:
        header = match[0]
        value = match[1]
        try:
            if value[-1] == ',':
                value = value[:-1]
            sorted_headers[header] = value
        except IndexError:
            pass
    return sorted_headers


if __name__ == "__main__":
    headers = """
Accept:
*/*
Accept-Encoding:
gzip, deflate, br
Accept-Language:
zh-CN,zh;q=0.9
Acs-Token:
1713960064881_1714043470481_bJ4QVrHxzYPAmK0J2SImvCKnkmU3oAMtGfAyJ/rBUsJNkje0N7/xqXnUh6J1YmcOYpWY8W4TYmld2lLI9iMJlAqxHHPtJSphJ7yjaHNEHHAt/g6TVEQTqHx7I+k7Y+uVTmJ2fO3nmv44ucEOgj2YdGyZfx1opspDMTapqBKEhe7CObpbgJaOzXnvxsTAF0iea2YhCdT7tMTHUI9RzTFY576nhwNKylyXEEswEQy0jiP9X6ETs7sVMzi7FgAAkeWNRFtFP0Tv360EswTcumpqQ8KfSd+uqmhmL751wNV4EOX1NtRWxTQSRQ0Ti/jFZNZB+FuXMknTeMb92I8r0Z0EgJUvX3zuwUQiJ/wt/89QyfnZR1XySdqaopTEEHJ7lBrUdRJt4bm3V0CjypubT+sorHh70r5LM/fznxPuItdGrh/gNUMbJmu3JCt4HeJyg8OJlA/UrVuYilyrkDVajWuXY9xUBA9Uxn580oX/DQ79ElffLa+TrRfOP820zpX6iH3m
Connection:
keep-alive
Content-Length:
188
Content-Type:
application/x-www-form-urlencoded; charset=UTF-8
Cookie:
BAIDUID=511FD7099381C5B66DB2E2C64D41E153:SL=0:NR=10:FG=1; MCITY=-131%3A; APPGUIDE_10_6_9=1; PSTM=1710208234; BIDUPSID=BAEB21C7E6C80EDD5E28B80EB5C2FA8A; APPGUIDE_10_7_0=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; APPGUIDE_10_7_1=1; APPGUIDE_10_7_2=1; smallFlowVersion=old; newlogin=1; H_WISE_SIDS=40302_40415_40446_40080_60131_60142; H_WISE_SIDS_BFESS=40302_40415_40446_40080_60131_60142; BA_HECTOR=2h248g01042h812g012k8524cm003e1j2i4l41t; BAIDUID_BFESS=511FD7099381C5B66DB2E2C64D41E153:SL=0:NR=10:FG=1; ZFY=IFd2i:AigfXURKPIa8hfvZ4qCISsDhm6TCrZEEUQ3tgM:C; H_PS_PSSID=40302_40415_40446_40080_60142; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1713928688,1713962815,1714008284,1714043414; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1714043436; ab_sr=1.0.1_OGVkNjFlZDEwODkwYTcwNzU4ZTQzMjU1MmVhYTAyMzcxMmM4YWQwMjM1YjkzZjhkMzExNmEzN2Q5OWI1YmI3MzNiYmU0ZjliOWMwZGIzYjA0OWM0MTgxYjcyMmViMWFjNzcxMDcwMjg1MzA0NTY1NDFlMzBjM2FlYzQ4ZTA2MDk1NDVkM2Q4YjMwN2Y5OTIyNmI0OWY4MzhjMmEzZDgxNw==
Host:
fanyi.baidu.com
Origin:
https://fanyi.baidu.com
Referer:
https://fanyi.baidu.com/?aldtype=16047
Sec-Ch-Ua:
"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"
Sec-Ch-Ua-Mobile:
?0
Sec-Ch-Ua-Platform:
"Windows"
Sec-Fetch-Dest:
empty
Sec-Fetch-Mode:
cors
Sec-Fetch-Site:
same-origin
User-Agent:
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36
X-Requested-With:
XMLHttpRequest

    
    
    """
    # 提取 头文件
    headers = extract_headers(headers)
    print(headers)

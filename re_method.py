# -*- coding = utf-8 -*-
# @Time : 2024/5/2 22:56
# @Author : 鬼鬼
# @File : re_method.py
# @Software: PyCharm


def re_use():

    import re
    import os.path
    path = ""
    front_path, origin_filename = os.path.split(path)

    # 使用正则表达式匹配中文字符
    china_font = re.compile(r'[\u4e00-\u9fa5]+')

    # result = china_font.findall(filename)
    # result = re.search(china_font, filename)

    # 将 匹配到的中文字符 用】 替换
    no_chinese_filename = re.sub(china_font, "】", origin_filename)




if __name__ == "__main__":

    pass

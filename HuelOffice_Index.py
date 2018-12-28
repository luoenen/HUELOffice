import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError,URLError

url_list = []
title_with_str = []
url_index = "http://jw.huel.edu.cn/"
def cd_index(url):
    html = urlopen(url)
    result = BeautifulSoup(html, 'html.parser')
    a_tag = result.find_all('a')
    for href in a_tag:
        url = str(href.get("href"))
        if str("http") in url:
            url_list.append(url)

def list_url(urls):
    for url in urls:
        if str("http://xk.huel.edu.cn/jwglxt") == url:
            continue
        titles = get_title(url)
        if titles is None:
            print("网页标题未找到！")
        else:
            for title in titles:
                title_with_str.append(title)
def get_title(url):
    try:
        html=urlopen(url)
    except (HTTPError,URLError) as e:
        print("网页提取错误：" + str(e))
        return None
    try:
        result=BeautifulSoup(html, 'html.parser')
        title=result.find_all('title')
    except AttributeError as e:
        print("网页提取错误："+str(e))
        return None
    return title

def show_title(titles_string, urls):
    titles_string.pop(2)
    urls.pop(2)
    index = 1
    for titles in  titles_string:
        key = str(titles)
        key = key.replace("\n","")
        key = key.replace("\r","")
        key = key.replace("\t","")
        key = key.replace(" ","")
        reg = r"(?<=<title>).+?(?=</title>)"
        pattern = re.compile(reg)
        matcher = re.search(pattern, key)
        title = matcher
        print(str(index)+":"+title.group(0))
        index+=1
    print(str(index)+":"+"河南财经政法大学教务信息服务平台")
    code = int(input("请输入从‘1’到‘9’的下标索引(纯数字)进入系统："))
    return str(code-1),urls

def get_code():
    return show_title(title_with_str,url_list)

cd_index(url_index)
list_url(url_list)


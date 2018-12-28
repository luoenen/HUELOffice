import re
import time
import requests
import random
from PIL import Image
from io import BytesIO
import webbrowser
from urllib.request import urlopen
from bs4 import BeautifulSoup
from HuelOffice_Student import pay_student,information_student
from HuelOffice_Code import cd_url,code

url = cd_url(code)

def url_one():
    webbrowser.open(url,new=2,autoraise=True)

def url_two():
    url_one()

def url_three():
    resp = urlopen(url)
    html = resp.read()
    soup = BeautifulSoup(html, "html.parser")
    result = soup.find(id="vsb_newscontent")
    img = re.findall(r'/\.\./(.+?)"', str(result))
    url_img = url[:22]+img[0]
    response = requests.get(url_img)
    image = Image.open(BytesIO(response.content))
    image.show()

def url_four():
    url_one()

def url_five():
    resp = urlopen(url)
    html = resp.read()
    soup = BeautifulSoup(html, "html.parser")
    result = soup.find(id="Image1")
    validate_text = re.findall(r'src="(.+?)"',str(result))
    validate_url = url+"/"+validate_text[0]+"?"+str(random.randint(116040282,916040282))
    response = requests.get(validate_url)
    image = Image.open(BytesIO(response.content))
    image.show()

def six():
    url_one()

def seven():
    url_one()

def eight():
    url_one()

def nine():
    information = "http://xk.huel.edu.cn/jwglxt/xtgl/login_slogin.html?language=zh_CN&_t="+str(int(time.time()))
    rsp = requests.Session()
    data = {
        "yhm": information_student.get("account"),
        "mm": information_student.get("password")
    }
    response = rsp.post(url=information,timeout=60, data=data)
    print(response.text)
url_one()

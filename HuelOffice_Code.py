
from HuelOffice_Index import get_code

urls = []
result = get_code()
code = result[0]
url_list = result[1]
for url in url_list:
    urls.append(url)

urls.append("http://xk.huel.edu.cn/jwglxt/xtgl/login_slogin.html")

def cd_url(index):

    print(len(urls))
    return urls[int(index)]






import urllib.request
import urllib.parse

url = 'http://www.vd.com/user/logCheck.php'

data = urllib.parse.urlencode({

    "user": "admin",
    "pass": "123456",
    "submit": "login"

}).encode("utf-8")

headers = {

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2"

}

# 进行POST请求，就需要使用 urllib.request 下面的 Request(地址,数据)
req = urllib.request.Request(url, headers=headers, data=data)

resut = urllib.request.urlopen(req).read().decode("utf-8")

print(resut)
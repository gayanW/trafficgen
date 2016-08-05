from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup

url = "https://www.whatismybrowser.com/developers/what-http-headers-is-my-browser-sending"
#url = "http://www.linuxdeveloper.space"

# http headers
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
referer = 'https://www.facebook.com/'
headers = {'User-Agent':user_agent, 'Referer':referer}

req = Request(url, headers=headers)
response = urlopen(req)

bsObj = BeautifulSoup(response.read(), 'lxml')


tableText = bsObj.find('table', {'class':'table-striped'}).get_text()
print(tableText)

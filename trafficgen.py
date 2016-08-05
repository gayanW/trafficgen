from urllib.request import urlopen
from urllib.request import Request
import time
#from bs4 import BeautifulSoup

#url = "https://www.whatismybrowser.com/developers/what-http-headers-is-my-browser-sending"
#url = "http://www.linuxdeveloper.space"
url = 'http://www.gossipocean.com'

# http headers
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome'
referers = ['https://www.facebook.com',
            'http://www.linuxdeveloper.space',
            'https://twitter.com']

# send request to url by each referer

for referer in referers:
    print('referer', referer)
    headers = {'User-Agent':user_agent, 'Referer':referer}
    req = Request(url, headers=headers)
    response = urlopen(req)

    print('{} >>\n'.format(referer), response.getheaders())
    time.sleep(10)


#bsObj = BeautifulSoup(response.read(), 'lxml')
#tableText = bsObj.find('table', {'class':'table-striped'}).get_text()
#print(tableText)

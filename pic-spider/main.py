'''request the page'''

import requests
import re
import time
import os

headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}          #in the chrome devtool network tag, page name, use the to  sumluate chrome. 个人身份

response = requests.get('https://www.vmgirls.com/13344.html',headers=headers) #put your link here
# print(response.request.headers)
html = response.text

''' analysis page '''
dir_name = re.findall('<h1 class="post-title h1">(.*?)</h1>',html)[-1]
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
urls = re.findall('<a href="(.*?)" alt=".*?" title=".*?"',html)
print(urls)

'''save image'''

for url in urls:
    time.sleep(0.2)
    url= 'https:' + url
    #pic name
    file_name = url.split('/')[-1]
    response = requests.get(url,headers=headers)
    with open(dir_name +'/' + file_name,'wb') as f:
        f.write(response.content)
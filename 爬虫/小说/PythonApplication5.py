import requests
from bs4 import BeautifulSoup
headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
        }
url_begin='https://www.bbiquge.net/book_682/766138.html' #网站的第一页
url=url_begin
for a in range(1,1628):  #章数加一
    r=requests.get(url,headers=headers,timeout=5)
    r.encoding='utf-8'
    soup=BeautifulSoup(r.content,"lxml")
    text_0=soup.find('div',id="main")
    text_1=text_0.find('div',id='content')
    head=soup.find('h1')
    file=open(str(head.string)+'.txt',"w",encoding='utf-8')
    for txt in text_1:
        txt=txt.get_text()
        txt=txt+'\n'
        file.write(txt)
    file.close
    re=soup.find('div',class_='papgbutton')
    print(str(head)+"成功")
    url_d=re.find_all('a')
    url_next=url_d[2].get("href")
    url=url_next

 




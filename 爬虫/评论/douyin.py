from DrissionPage import ChromiumPage
from time import sleep
import pandas as pd

keyword = '男生'
max_comment = 20

row = []

page = ChromiumPage()
page.get('https://www.douyin.com/?recommend=1')
search_box = page.ele(".st2xnJtZ YIde9aUh")
search_box.input(keyword)
sleep(0.5)
page.ele(".JMEzcqbO").click()
sleep(2)
tab = page.get_tab(page.latest_tab)
sleep(2)
ks = tab.ele(".jNZ2JfiY")
ks.click()
ks.click()
sleep(0.5)
ks.ele('text=最多点赞').click()
sleep(2)
list_video = tab.eles('.YkcX1IuK')
for video_number in range(len(list_video)):
    list_video = tab.eles('.YkcX1IuK')  #解决元素丢失问题
    video = list_video[video_number]
    video.click()
    sleep(0.5)
    tab.ele('.tzVl3l7w').click()     
    sleep(2)
    scrool_a = tab.ele('.sX7gMtFl comment-mainContent MR0IFMr1')
    number_comment =0
    while True:
        scrool_a.scroll.down(1000)
        sleep(1)
        number_comment += 1
        if page.ele('.BbQpYS5o',timeout = 0.5) == 1 or number_comment == max_comment:
            break
    all_comment = tab.ele('.sX7gMtFl comment-mainContent MR0IFMr1')
    comments = all_comment.eles('.CDx534Ub')
    title = tab.ele('.Nu66P_ba xhDopcQ_ Jn1tVXor').text
    if len(title) >10:
        title = title[:10]
    for k in comments:
        name = k.ele('.Nu66P_ba NCRZnxVF').text
        the_comment = k.ele('.a9uirtCT').text
        like = k.ele('.eJuDTubq').text
        row.append({'用户名':name,'评论':the_comment,'点赞数':like,'平台':'抖音'})
    df=pd.DataFrame(row)
    df.to_csv(title+'.csv',encoding="utf_8_sig")
    tab.ele('.bFdMjgdW').click()
    sleep(2)

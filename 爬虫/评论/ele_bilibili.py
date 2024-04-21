from DrissionPage import ChromiumPage
from DrissionPage import ChromiumOptions
from time import sleep
import time
import pandas as pd

web_url = 'https://www.bilibili.com/video/BV1yZ421v7c6/?spm_id_from=333.1007.top_right_bar_window_dynamic.content.click&vd_source=0c06d37438de995b3857bfea2ddab094'

max_comment = 20
co = ChromiumOptions()
co.no_imgs(True)
page = ChromiumPage(co)
page.get(web_url)
sleep(4)
row = []
title = page.ele('.video-info-title').text
while True:
    page.scroll.to_bottom()   
    sleep(2)
    if bool(page.ele('.reply-end',timeout = 0.5)) == True:
        break

main_comment = page.eles('.content-warp')
for dk in main_comment:
    the_name = dk.ele(".user-name").text
    the_comment = dk.ele('.reply-content').text
    number_like = dk.ele('.reply-like').text
    if number_like is False:
        number_like = '0'
    row.append({'用户名':the_name,'评论':the_comment,'like':number_like,'平台':'bilibili'})

df=pd.DataFrame(row)
if len(title)>10:
    title = title[:8]
df.to_csv(title+'.csv',encoding="utf_8_sig")
from DrissionPage import ChromiumPage
from time import sleep
import pandas as pd

keyword = '彩礼'
max_comment = 20

row = []

page = ChromiumPage()
page.get('https://www.xiaohongshu.com/explore')
sleep(5)
search_box = page.ele("#search-input")
search_box.input(keyword)
sleep(0.5)
page.ele(".search-icon").click()
sleep(0.5)
page.ele(".filter-box").click()
sleep(0.5)
page.ele("xpath:/html/body/div[4]/div/li[3]").click()
sleep(4)
a_list = page.eles('.cover ld mask')
print(a_list)
for i in range(0,len(a_list)):
    a_list = page.eles('.cover ld mask')  #不加此条会导致下次循环元素丢失，所以要重新找一次
    papaer = a_list[i]
    sleep(0.5)
    papaer.click()
    scroll_a = page.ele('.note-scroller')
    title = page.ele('.title').text
    
    main_name = page.ele('.username').text
    main_comment = page.ele('.desc').text
    main_agree = page.ele('.count').text
    main_list = [main_name,main_comment,0]
    row.append({'用户名':main_name,'评论':main_comment,'点赞数':main_agree,'平台':'小红书'})
    number_comment = 0
    while True:
        scroll_a.scroll.down(1000)
        sleep(0.5)
        number_comment += 1
        if page.ele('.end-container',timeout = 0.5) == 1 or number_comment == max_comment:
            break
    sleep(1)
    comments = page.eles('.parent-comment')
    for comment in comments:
        commenter_name = comment.ele('.name').text
        agree_num = comment.ele('.count').text
        ob = comment.ele('.content').text
        row.append({'用户名':commenter_name,'评论':ob,'点赞数':agree_num,'平台':'小红书'})
        
    df=pd.DataFrame(row)
    df.to_csv(title+'.csv',encoding="utf_8_sig")
    page.ele('.close close-mask-dark').click()
    print('主爬取完毕')
    sleep(1)
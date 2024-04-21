from DrissionPage import ChromiumPage
from DrissionPage import ChromiumOptions
from time import sleep
import time
import pandas as pd

keyword = '相亲'
max_comment = 20




co = ChromiumOptions()
co.no_imgs(True)
page = ChromiumPage(co)
page.get('https://tieba.baidu.com/')
sleep(4)
search_box = page.ele("#wd1")
search_box.input(keyword)
sleep(0.5)
page.ele(".search_btn_wrap search_btn_enter_ba_wrap").click()
sleep(3)

def go_baidu():
    a_list = page.eles('. j_thread_list clearfix thread_item_box')
    for i in range(len(a_list)):
        row = []
        papaer = a_list[i]
        num_answer = papaer.ele(".threadlist_rep_num center_text").text
        if int(num_answer) >= 100:
            title = papaer.ele('.threadlist_title pull_left j_th_tit ').text
            papaer.ele('.j_th_tit ').click()
            sleep(3)
            tab = page.get_tab(page.latest_tab)
            while True:
                tab.scroll.to_bottom()
                sleep(1.5)
                all_comment = tab.eles('.l_post l_post_bright j_l_post clearfix  ')
                for comment_a in all_comment:
                    if bool(comment_a.s_ele('.p_author_name j_user_card')) == True:
                        user_name = comment_a.s_ele('.p_author_name j_user_card').text
                    elif bool(comment_a.s_ele('.p_author_name j_user_card vip_red ')) == True:
                        user_name = comment_a.s_ele('.p_author_name j_user_card vip_red ').text
                    elif bool(comment_a.s_ele('.p_author_name sign_highlight j_user_card')) == True:
                        user_name = comment_a.s_ele('.p_author_name sign_highlight j_user_card').text
                    the_comment = comment_a.s_ele('.d_post_content j_d_post_content ')

                    if bool(the_comment.text) == False:
                        main_comment = '图片'
                    else:
                        main_comment = the_comment.text
                        row.append({'用户名':user_name,'评论':main_comment,'平台':'百度贴吧'+keyword})

                dns = tab.ele('.l_pager pager_theme_5 pb_list_pager')
                c = dns.ele('text:下一页')
                if bool(c) == True:
                    c.click()
                    sleep(2)
                else:
                    break
            df=pd.DataFrame(row)
            df.to_csv(title+'.csv',encoding="utf_8_sig")
            tab.close()
        else:
            pass
for i in range(2):
    go_baidu()
    page.scroll.to_bottom()
    page.ele('.next pagination-item ').click()
    sleep(3)


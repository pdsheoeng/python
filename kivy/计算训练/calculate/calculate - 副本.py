from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.resources import resource_add_path
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.properties import StringProperty
import random
from time import strftime

resource_add_path('./fonts')  # 全局申明载入字体
LabelBase.register(DEFAULT_FONT, 'font.ttf')


Builder.load_string("""
<MenuScreen>:
    name:'menu'
    BoxLayout:
        font_size: dp(80)
        orientation: 'vertical'
        Label:
            markup: True
            text:'      计  算  训  练[sub]--pdsheoeng[/sub]'
            size: self.texture_size
            font_size:30
            color:0.4,0.4,1,1
        Button:
            text:'加  法'
            font_size:30
            color:0.4,0.4,1,1
            background_color:0,0,0,1
            on_press:
                root.manager.current='Addition'
        Button:
            text:'减  法'
            font_size:30
            color:0.4,0.4,1,1
            background_color:0,0,0,1
            on_press:
                root.manager.current='Subtraction'
        Button:
            text:'乘  法'
            font_size:30
            color:0.4,0.4,1,1
            background_color:0,0,0,1
            on_press:
                root.manager.current='Multiplication'
        Button:
            text:'除  法'
            font_size:30
            color:0.4,0.4,1,1
            background_color:0,0,0,1
            on_press:
                root.manager.current='Division'
        Button:
            text:'历史记录'
            font_size:30
            color:0.4,0.4,1,1
            background_color:0,0,0,1
            on_press:
                root.manager.current='LS'

<LogScreen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text:'做题数量达到一万解锁'
            font_size:40
            color:0.4,0.4,1,1
        Label:
            text:'2022/9/6完成 耗时2天 '
            font_size:40
            color:0.4,0.4,1,1
        Label:
            text:'Thank you for using it'
            font_size:40
            color:0.4,0.4,1,1
    

<AdditionScreen>:
    BoxLayout:
        orientation: 'vertical'
        Button:
            text:'加法初级'
            font_size:30
            color:0.4,0.4,1,1
            background_color:0,0,0,1
            on_press:
                root.manager.current='A1'
        Button:
            text:'加法中级'
            font_size:30
            color:0.4,0.4,1,1
            background_color:0,0,0,1
            on_press:
                root.manager.current='A2'
        Button:
            text:'加法高级'
            font_size:30
            color:0.4,0.4,1,1
            background_color:0,0,0,1
            on_press:
                root.manager.current='A3'
        Button:
            text:'返回'
            font_size:30
            color:0.4,0.4,1,1
            background_color:0,0,0,1
            on_press:
                root.manager.current='menu'

<SubtractionScreen>:
    BoxLayout:
        orientation: 'vertical'
        Button:
            text:'减法初级'
            font_size:30
            color:0.4,0.4,1,1
            background_color:0,0,0,1
            on_press:
                root.manager.current='S1'
        Button:
            text:'减法中级'
            font_size:30
            color:0.4,0.4,1,1
            background_color:0,0,0,1
            on_press:
                root.manager.current='S2'
        Button:
            text:'减法高级'
            font_size:30
            color:0.4,0.4,1,1
            background_color:0,0,0,1
            on_press:
                root.manager.current='S3'
        Button:
            text:'返回'
            font_size:30
            color:0.4,0.4,1,1
            background_color:0,0,0,1
            on_press:
                root.manager.current='menu'
    

<MultiplicationScreen>:
    BoxLayout:
        orientation: 'vertical'
        Button:
            text:'乘法初级'
            font_size:30
            color:0.4,0.4,1,1
            background_color:0,0,0,1
            on_press:
                root.manager.current='M1'
        Button:
            text:'乘法中级'
            font_size:30
            color:0.4,0.4,1,1
            background_color:0,0,0,1
            on_press:
                root.manager.current='M2'
        Button:
            text:'乘法高级'
            font_size:30
            color:0.4,0.4,1,1
            background_color:0,0,0,1
            on_press:
                root.manager.current='M3'
        Button:
            text:'返回'
            font_size:30
            color:0.4,0.4,1,1
            background_color:0,0,0,1
            on_press:
                root.manager.current='menu'

<DivisionScreen>:
    BoxLayout:
        orientation: 'vertical'
        Button:
            text:'除法初级'
            font_size:30
            color:0.4,0.4,1,1
            background_color:0,0,0,1
            on_press:
                root.manager.current='D1'
        Button:
            text:'除法中级'
            font_size:30
            color:0.4,0.4,1,1
            background_color:0,0,0,1
            on_press:
                root.manager.current='D2'
        Button:
            text:'除法高级'
            font_size:30
            color:0.4,0.4,1,1
            background_color:0,0,0,1
            on_press:
                root.manager.current='D3'
        Button:
            text:'返回'
            font_size:30
            color:0.4,0.4,1,1
            background_color:0,0,0,1
            on_press:
                root.manager.current='menu'

<Addition1Screen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            id:time
            markup:True
            text:'所用时间：[b]00[/b]:00:00'
            font_size:30
        Label:
            font_size:30
            id:text_update
            text:root.record
        Label:
            id:labelA
            font_size:30
            text:root.asking
        TextInput:
            font_size:30
            id:A1
            text:''
        Button:
            id:start
            font_size:30
            text:root.word
            background_color:0.2,0.2,0.8,1
            on_press:
                root.yorn(A1.text)
                root.begin()
                root.start_on_stop()
        Button:
            id:x2
            font_size:30
            background_color:0,0,0,1
            text:'点击蓝色开始，点此处结算'
            on_press:
                root.restartscreen()

<Addition2Screen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            id:time
            markup:True
            text:'所用时间：[b]00[/b]:00:00'
            font_size:30
        Label:
            font_size:30
            id:text_update
            text:root.record
        Label:
            id:labelA
            font_size:30
            text:root.asking
        TextInput:
            font_size:30
            id:A1
            text:''
        Button:
            id:start
            font_size:30
            text:root.word
            background_color:0.2,0.2,0.8,1
            on_press:
                root.yorn(A1.text)
                root.begin()
                root.start_on_stop()
        Button:
            id:x2
            font_size:30
            background_color:0,0,0,1
            text:'点击蓝色开始，点此处结算'
            on_press:
                root.restartscreen()

<Addition3Screen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            id:time
            markup:True
            text:'所用时间：[b]00[/b]:00:00'
            font_size:30
        Label:
            font_size:30
            id:text_update
            text:root.record
        Label:
            id:labelA
            font_size:30
            text:root.asking
        TextInput:
            font_size:30
            id:A2
            text:''
        Button:
            id:start
            font_size:30
            text:root.word
            background_color:0.2,0.2,0.8,1
            on_press:
                root.yorn(A2.text)
                root.begin()
                root.start_on_stop()
        Button:
            id:x2
            font_size:30
            background_color:0,0,0,1
            text:'点击蓝色开始，点此处结算'
            on_press:
                root.restartscreen()

<Subtraction1Screen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            id:time
            markup:True
            text:'所用时间：[b]00[/b]:00:00'
            font_size:30
        Label:
            font_size:30
            id:text_update
            text:root.record
        Label:
            id:labelA
            font_size:30
            text:root.asking
        TextInput:
            font_size:30
            id:A2
            text:''
        Button:
            id:start
            font_size:30
            text:root.word
            background_color:0.2,0.2,0.8,1
            on_press:
                root.yorn(A2.text)
                root.begin()
                root.start_on_stop()
        Button:
            id:x2
            font_size:30
            background_color:0,0,0,1
            text:'点击蓝色开始，点此处结算'
            on_press:
                root.restartscreen()

<Subtraction2Screen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            id:time
            markup:True
            text:'所用时间：[b]00[/b]:00:00'
            font_size:30
        Label:
            font_size:30
            id:text_update
            text:root.record
        Label:
            id:labelA
            font_size:30
            text:root.asking
        TextInput:
            font_size:30
            id:A2
            text:''
        Button:
            id:start
            font_size:30
            text:root.word
            background_color:0.2,0.2,0.8,1
            on_press:
                root.yorn(A2.text)
                root.begin()
                root.start_on_stop()
        Button:
            id:x2
            font_size:30
            background_color:0,0,0,1
            text:'点击蓝色开始，点此处结算'
            on_press:
                root.restartscreen()

<Subtraction3Screen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            id:time
            markup:True
            text:'所用时间：[b]00[/b]:00:00'
            font_size:30
        Label:
            font_size:30
            id:text_update
            text:root.record
        Label:
            id:labelA
            font_size:30
            text:root.asking
        TextInput:
            font_size:30
            id:A2
            text:''
        Button:
            id:start
            font_size:30
            text:root.word
            background_color:0.2,0.2,0.8,1
            on_press:
                root.yorn(A2.text)
                root.begin()
                root.start_on_stop()
        Button:
            id:x2
            font_size:30
            background_color:0,0,0,1
            text:'点击蓝色开始，点此处结算'
            on_press:
                root.restartscreen()

<Multiplication_1Screen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            id:time
            markup:True
            text:'所用时间：[b]00[/b]:00:00'
            font_size:30
        Label:
            font_size:30
            id:text_update
            text:root.record
        Label:
            id:labelA
            font_size:30
            text:root.asking
        TextInput:
            font_size:30
            id:A2
            text:''
        Button:
            id:start
            font_size:30
            text:root.word
            background_color:0.2,0.2,0.8,1
            on_press:
                root.yorn(A2.text)
                root.begin()
                root.start_on_stop()
        Button:
            id:x2
            font_size:30
            background_color:0,0,0,1
            text:'点击蓝色开始，点此处结算'
            on_press:
                root.restartscreen()

<Multiplication_2Screen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            id:time
            markup:True
            text:'所用时间：[b]00[/b]:00:00'
            font_size:30
        Label:
            font_size:30
            id:text_update
            text:root.record
        Label:
            id:labelA
            font_size:30
            text:root.asking
        TextInput:
            font_size:30
            id:A2
            text:''
        Button:
            id:start
            font_size:30
            text:root.word
            background_color:0.2,0.2,0.8,1
            on_press:
                root.yorn(A2.text)
                root.begin()
                root.start_on_stop()
        Button:
            id:x2
            font_size:30
            background_color:0,0,0,1
            text:'点击蓝色开始，点此处结算'
            on_press:
                root.restartscreen()

<Multiplication_3Screen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            id:time
            markup:True
            text:'所用时间：[b]00[/b]:00:00'
            font_size:30
        Label:
            font_size:30
            id:text_update
            text:root.record
        Label:
            id:labelA
            font_size:30
            text:root.asking
        TextInput:
            font_size:30
            id:A2
            text:''
        Button:
            id:start
            font_size:30
            text:root.word
            background_color:0.2,0.2,0.8,1
            on_press:
                root.yorn(A2.text)
                root.begin()
                root.start_on_stop()
        Button:
            id:x2
            font_size:30
            background_color:0,0,0,1
            text:'点击蓝色开始，点此处结算'
            on_press:
                root.restartscreen()

<Division_1Screen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            id:time
            markup:True
            text:'所用时间：[b]00[/b]:00:00'
            font_size:30
        Label:
            font_size:30
            id:text_update
            text:root.record
        Label:
            id:labelA
            font_size:30
            text:root.asking
        TextInput:
            font_size:30
            id:A2
            text:''
        Button:
            id:start
            font_size:30
            text:root.word
            background_color:0.2,0.2,0.8,1
            on_press:
                root.yorn(A2.text)
                root.begin()
                root.start_on_stop()
        Button:
            id:x2
            font_size:30
            background_color:0,0,0,1
            text:'点击蓝色开始，点此处结算'
            on_press:
                root.restartscreen()

<Division_2Screen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            id:time
            markup:True
            text:'所用时间：[b]00[/b]:00:00'
            font_size:30
        Label:
            font_size:30
            id:text_update
            text:root.record
        Label:
            id:labelA
            font_size:30
            text:root.asking
        TextInput:
            font_size:30
            id:A2
            text:''
        Button:
            id:start
            font_size:30
            text:root.word
            background_color:0.2,0.2,0.8,1
            on_press:
                root.yorn(A2.text)
                root.begin()
                root.start_on_stop()
        Button:
            id:x2
            font_size:30
            background_color:0,0,0,1
            text:'点击蓝色开始，点此处结算'
            on_press:
                root.restartscreen()

<Division_3Screen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            id:time
            markup:True
            text:'所用时间：[b]00[/b]:00:00'
            font_size:30
        Label:
            font_size:30
            id:text_update
            text:root.record
        Label:
            id:labelA
            font_size:30
            text:root.asking
        TextInput:
            font_size:30
            id:A2
            text:''
        Button:
            id:start
            font_size:30
            text:root.word
            background_color:0.2,0.2,0.8,1
            on_press:
                root.yorn(A2.text)
                root.begin()
                root.start_on_stop()
        Button:
            id:x2
            font_size:30
            background_color:0,0,0,1
            text:'点击蓝色开始，点此处结算'
            on_press:
                root.restartscreen()


""")


class MenuScreen(Screen):
    pass

class AdditionScreen(Screen):
    pass

class SubtractionScreen(Screen):
    pass
class MultiplicationScreen(Screen):
    pass
class DivisionScreen(Screen):
    pass
class LogScreen(Screen):
    pass

class Addition1Screen(Screen):

    record = StringProperty()
    asking = StringProperty()
    word = StringProperty()
    


    def __init__(self, **kwargs):
        super(Addition1Screen, self).__init__(**kwargs)
        self.timing_flag = False
        self.timing_seconds = 0
        self.answer=0
        self.sto=0
        self.sta = 0
        self.st=0
        self.endtime = ''
        self.on_start()
 
    def on_start(self):
        # 设置clock 每0秒执行一次，代表实时进行不间断刷新。
        Clock.schedule_interval(self.update_time, 0)
 
    def update_time(self, nap):
        if self.timing_flag:
            self.timing_seconds += nap

        m, s = divmod(self.timing_seconds, 60)
        self.ids.time.text = ('%02d:%02d.[size=40]%02d[/size]' % (int(m), int(s), int(s * 100 % 100)))

    def start_on_stop(self):
        self.timing_flag = True
 

    def begin(self):
        self.a=random.randint(10,99)
        self.b=random.randint(10,99)
        self.answer=self.a+self.b
        asking=str(self.a)+'+'+str(self.b)+'='

        self.asking=asking


    def yorn(self,number):
        
        if self.timing_flag == False :
            self.timing_seconds = 0
        self.st = 0
        self.ids.A1.text = ''
        answer=self.answer
        num=number
        if num != '' :
            if int(num)==int(answer): #注意这里answer是字符，不过不加int()会一直判定为假
                self.sta = self.sta + 1 
            else:
                pass

        self.word='提交'
        self.sto=self.sto+1
        num_do=self.sto
        self.record='已做题目数量:'+str(num_do-1)
        self.word=self.word
        self.ids.x2.text = '点击蓝色开始，点此处结算'


    def restartscreen(self):

        
        self.endtime = ''
        self.st = self.st + 1
        self.ids.x2.text = '返回主页'
        self.ids.text_update.text = '一共做了 '+str(self.sto-1)+'道题，对了'+str(self.sta)+'道题'
        if self.sto >= 10:           
            if float(self.sta)/float(self.sto-1) < 0.6 :
                self.ids.labelA.text = '太菜了！（￣へ￣）'
            if  0.6 < float(self.sta)/float(self.sto-1) <= 0.8 :
                self.ids.labelA.text = '再接再厉┐(￣ヮ￣)┌'
            if float(self.sta)/float(self.sto-1) > 0.8:
                self.ids.labelA.text = '厉害捏! (°Д°) '
        if self.sto < 10 :
            self.ids.labelA.text = '才做这点题就不想做了? (⊙_⊙)'
        if self.st >= 2:
            self.timing_seconds = 0
            self.ids.time.text = '00:00:00'
            self.manager.current = 'menu'
            self.word='提交'
            self.ids.x2.text = '点击蓝色开始，点此处结算'
            self.ids.text_update.text = '别卷了！求求你了！(ㄒoㄒ) '
            self.ids.labelA.text = '别卷了！求求你了！(ㄒoㄒ) '
        self.timing_flag = False
        self.word = '重新开始'
        self.sta = 0
        self.sto=0



    pass

class Addition2Screen(Screen):

    record = StringProperty()
    asking = StringProperty()
    word = StringProperty()
    


    def __init__(self, **kwargs):
        super(Addition2Screen, self).__init__(**kwargs)
        self.timing_flag = False
        self.timing_seconds = 0
        self.answer=0
        self.sto=0
        self.sta = 0
        self.st=0
        self.endtime = ''
        self.on_start()
 
    def on_start(self):
        # 设置clock 每0秒执行一次，代表实时进行不间断刷新。
        Clock.schedule_interval(self.update_time, 0)
 
    def update_time(self, nap):
        if self.timing_flag:
            self.timing_seconds += nap

        m, s = divmod(self.timing_seconds, 60)
        self.ids.time.text = ('%02d:%02d.[size=40]%02d[/size]' % (int(m), int(s), int(s * 100 % 100)))

    def start_on_stop(self):
        self.timing_flag = True
 

    def begin(self):
        self.a=random.randint(100,999)
        self.b=random.randint(100,999)
        self.answer=self.a+self.b
        asking=str(self.a)+'+'+str(self.b)+'='

        self.asking=asking


    def yorn(self,number):
        
        if self.timing_flag == False :
            self.timing_seconds = 0
        self.st = 0
        self.ids.A1.text = ''
        answer=self.answer
        num=number
        if num != '' :
            if int(num)==int(answer): #注意这里answer是字符，不过不加int()会一直判定为假
                self.sta = self.sta + 1 
            else:
                pass

        self.word='提交'
        self.sto=self.sto+1
        num_do=self.sto
        self.record='已做题目数量:'+str(num_do-1)
        self.word=self.word
        self.ids.x2.text = '点击蓝色开始，点此处结算'


    def restartscreen(self):

        
        self.endtime = ''
        self.st = self.st + 1
        self.ids.x2.text = '返回主页'
        self.ids.text_update.text = '一共做了 '+str(self.sto-1)+'道题，对了'+str(self.sta)+'道题'
        if self.sto >= 10:           
            if float(self.sta)/float(self.sto-1) < 0.6 :
                self.ids.labelA.text = '太菜了！（￣へ￣）'
            if  0.6 < float(self.sta)/float(self.sto-1) <= 0.8 :
                self.ids.labelA.text = '再接再厉┐(￣ヮ￣)┌'
            if float(self.sta)/float(self.sto-1) > 0.8:
                self.ids.labelA.text = '厉害捏! (°Д°) '
        if self.sto < 10 :
            self.ids.labelA.text = '才做这点题就不想做了? (⊙_⊙)'
        if self.st >= 2:
            self.timing_seconds = 0
            self.ids.time.text = '00:00:00'
            self.manager.current = 'menu'
            self.word='提交'
            self.ids.x2.text = '点击蓝色开始，点此处结算'
            self.ids.text_update.text = '别卷了！求求你了！(ㄒoㄒ) '
            self.ids.labelA.text = '别卷了！求求你了！(ㄒoㄒ) '
        self.timing_flag = False
        self.word = '重新开始'
        self.sta = 0
        self.sto=0



    pass

class Addition3Screen(Screen):


    record = StringProperty()
    asking = StringProperty()
    word = StringProperty()
    


    def __init__(self, **kwargs):
        super(Addition3Screen, self).__init__(**kwargs)
        self.timing_flag = False
        self.timing_seconds = 0
        self.answer=0
        self.sto= 0
        self.sta = 0
        self.st=0
        self.endtime = ''
        self.on_start()
 
    def on_start(self):
        # 设置clock 每0秒执行一次，代表实时进行不间断刷新。
        Clock.schedule_interval(self.update_time, 0)
 
    def update_time(self, nap):
        if self.timing_flag:
            self.timing_seconds += nap

        m, s = divmod(self.timing_seconds, 60)
        self.ids.time.text = ('%02d:%02d.[size=40]%02d[/size]' % (int(m), int(s), int(s * 100 % 100)))

    def start_on_stop(self):
        self.timing_flag = True
 

    def begin(self):
        self.a=random.randint(999,9999)
        self.b=random.randint(999,9999)
        self.answer=self.a+self.b
        asking=str(self.a)+'+'+str(self.b)+'='

        self.asking=asking


    def yorn(self,number):
        
        if self.timing_flag == False :
            self.timing_seconds = 0
        self.st = 0
        self.ids.A2.text = ''
        answer=self.answer
        num=number
        if num != '' :
            if int(num)==int(answer): #注意这里answer是字符，不过不加int()会一直判定为假
                self.sta = self.sta + 1 
            else:
                pass

        self.word='提交'
        self.sto=self.sto+1
        num_do=self.sto
        self.record='已做题目数量:'+str(num_do-1)
        self.word=self.word
        self.ids.x2.text = '点击蓝色开始，点此处结算'


    def restartscreen(self):

        self.endtime = ''
        self.st = self.st + 1
        self.ids.x2.text = '返回主页'
        self.ids.text_update.text = '一共做了 '+str(self.sto-1)+'道题，对了'+str(self.sta)+'道题'
        if self.sto >= 10:           
            if float(self.sta)/float(self.sto-1) < 0.6 :
                self.ids.labelA.text = '太菜了！（￣へ￣）'
            if  0.6 < float(self.sta)/float(self.sto-1) <= 0.8 :
                self.ids.labelA.text = '再接再厉┐(￣ヮ￣)┌'
            if float(self.sta)/float(self.sto-1) > 0.8:
                self.ids.labelA.text = '厉害捏! (°Д°) '
        if self.sto < 10 :
            self.ids.labelA.text = '才做这点题就不想做了? (⊙_⊙)'
        if self.st >= 2:
            self.timing_seconds = 0
            self.ids.time.text = '00:00:00'
            self.manager.current = 'menu'
            self.word='提交'
            self.ids.x2.text = '点击蓝色开始，点此处结算'
            self.ids.text_update.text = '别卷了！求求你了！(ㄒoㄒ) '
            self.ids.labelA.text = '别卷了！求求你了！(ㄒoㄒ) '
        self.timing_flag = False
        self.word = '重新开始'
        self.sta = 0
        self.sto=0








    pass

class Subtraction1Screen(Screen):


    record = StringProperty()
    asking = StringProperty()
    word = StringProperty()
    


    def __init__(self, **kwargs):
        super(Subtraction1Screen, self).__init__(**kwargs)
        self.timing_flag = False
        self.timing_seconds = 0
        self.answer=0
        self.sto  = 0
        self.sta = 0
        self.st=0
        self.endtime = ''
        self.on_start()
 
    def on_start(self):
        # 设置clock 每0秒执行一次，代表实时进行不间断刷新。
        Clock.schedule_interval(self.update_time, 0)
 
    def update_time(self, nap):
        if self.timing_flag:
            self.timing_seconds += nap

        m, s = divmod(self.timing_seconds, 60)
        self.ids.time.text = ('%02d:%02d.[size=40]%02d[/size]' % (int(m), int(s), int(s * 100 % 100)))

    def start_on_stop(self):
        self.timing_flag = True
 

    def begin(self):
        self.a=random.randint(9,99)
        self.b=random.randint(9,99)
        self.answer=self.a-self.b
        asking=str(self.a)+'-'+str(self.b)+'='

        self.asking=asking


    def yorn(self,number):
        
        if self.timing_flag == False :
            self.timing_seconds = 0
        self.st = 0
        self.ids.A2.text = ''
        answer=self.answer
        num=number
        if num != '' :
            if int(num)==int(answer): #注意这里answer是字符，不过不加int()会一直判定为假
                self.sta = self.sta + 1 
            else:
                pass

        self.word='提交'
        self.sto=self.sto+1
        num_do=self.sto
        self.record='已做题目数量:'+str(num_do-1)
        self.word=self.word
        self.ids.x2.text = '点击蓝色开始，点此处结算'


    def restartscreen(self):

        self.endtime = ''
        self.st = self.st + 1
        self.ids.x2.text = '返回主页'
        self.ids.text_update.text = '一共做了 '+str(self.sto-1)+'道题，对了'+str(self.sta)+'道题'
        if self.sto >= 10:           
            if float(self.sta)/float(self.sto-1) < 0.6 :
                self.ids.labelA.text = '太菜了！（￣へ￣）'
            if  0.6 < float(self.sta)/float(self.sto-1) <= 0.8 :
                self.ids.labelA.text = '再接再厉┐(￣ヮ￣)┌'
            if float(self.sta)/float(self.sto-1) > 0.8:
                self.ids.labelA.text = '厉害捏! (°Д°) '
        if self.sto < 10 :
            self.ids.labelA.text = '才做这点题就不想做了? (⊙_⊙)'
        if self.st >= 2:
            self.timing_seconds = 0
            self.ids.time.text = '00:00:00'
            self.manager.current = 'menu'
            self.word='提交'
            self.ids.x2.text = '点击蓝色开始，点此处结算'
            self.ids.text_update.text = '别卷了！求求你了！(ㄒoㄒ) '
            self.ids.labelA.text = '别卷了！求求你了！(ㄒoㄒ) '
        self.timing_flag = False
        self.word = '重新开始'
        self.sta = 0
        self.sto  = 0








    pass

class Subtraction2Screen(Screen):


    record = StringProperty()
    asking = StringProperty()
    word = StringProperty()
    


    def __init__(self, **kwargs):
        super(Subtraction2Screen, self).__init__(**kwargs)
        self.timing_flag = False
        self.timing_seconds = 0
        self.answer=0
        self.sto  = 0
        self.sta = 0
        self.st=0
        self.endtime = ''
        self.on_start()
 
    def on_start(self):
        # 设置clock 每0秒执行一次，代表实时进行不间断刷新。
        Clock.schedule_interval(self.update_time, 0)
 
    def update_time(self, nap):
        if self.timing_flag:
            self.timing_seconds += nap

        m, s = divmod(self.timing_seconds, 60)
        self.ids.time.text = ('%02d:%02d.[size=40]%02d[/size]' % (int(m), int(s), int(s * 100 % 100)))

    def start_on_stop(self):
        self.timing_flag = True
 

    def begin(self):
        self.a=random.randint(99,999)
        self.b=random.randint(99,999)
        self.answer=self.a-self.b
        asking=str(self.a)+'-'+str(self.b)+'='

        self.asking=asking


    def yorn(self,number):
        
        if self.timing_flag == False :
            self.timing_seconds = 0
        self.st = 0
        self.ids.A2.text = ''
        answer=self.answer
        num=number
        if num != '' :
            if int(num)==int(answer): #注意这里answer是字符，不过不加int()会一直判定为假
                self.sta = self.sta + 1 
            else:
                pass

        self.word='提交'
        self.sto=self.sto+1
        num_do=self.sto
        self.record='已做题目数量:'+str(num_do-1)
        self.word=self.word
        self.ids.x2.text = '点击蓝色开始，点此处结算'


    def restartscreen(self):

        self.endtime = ''
        self.st = self.st + 1
        self.ids.x2.text = '返回主页'
        self.ids.text_update.text = '一共做了 '+str(self.sto-1)+'道题，对了'+str(self.sta)+'道题'
        if self.sto >= 10:           
            if float(self.sta)/float(self.sto-1) < 0.6 :
                self.ids.labelA.text = '太菜了！（￣へ￣）'
            if  0.6 < float(self.sta)/float(self.sto-1) <= 0.8 :
                self.ids.labelA.text = '再接再厉┐(￣ヮ￣)┌'
            if float(self.sta)/float(self.sto-1) > 0.8:
                self.ids.labelA.text = '厉害捏! (°Д°) '
        if self.sto < 10 :
            self.ids.labelA.text = '才做这点题就不想做了? (⊙_⊙)'
        if self.st >= 2:
            self.timing_seconds = 0
            self.ids.time.text = '00:00:00'
            self.manager.current = 'menu'
            self.word='提交'
            self.ids.x2.text = '点击蓝色开始，点此处结算'
            self.ids.text_update.text = '别卷了！求求你了！(ㄒoㄒ) '
            self.ids.labelA.text = '别卷了！求求你了！(ㄒoㄒ) '
        self.timing_flag = False
        self.word = '重新开始'
        self.sta = 0
        self.sto  = 0








    pass

class Subtraction3Screen(Screen):


    record = StringProperty()
    asking = StringProperty()
    word = StringProperty()
    


    def __init__(self, **kwargs):
        super(Subtraction3Screen, self).__init__(**kwargs)
        self.timing_flag = False
        self.timing_seconds = 0
        self.answer=0
        self.sto  = 0
        self.sta = 0
        self.st=0
        self.endtime = ''
        self.on_start()
 
    def on_start(self):
        # 设置clock 每0秒执行一次，代表实时进行不间断刷新。
        Clock.schedule_interval(self.update_time, 0)
 
    def update_time(self, nap):
        if self.timing_flag:
            self.timing_seconds += nap

        m, s = divmod(self.timing_seconds, 60)
        self.ids.time.text = ('%02d:%02d.[size=40]%02d[/size]' % (int(m), int(s), int(s * 100 % 100)))

    def start_on_stop(self):
        self.timing_flag = True
 

    def begin(self):
        self.a=random.randint(999,9999)
        self.b=random.randint(999,9999)
        self.answer=self.a-self.b
        asking=str(self.a)+'-'+str(self.b)+'='

        self.asking=asking


    def yorn(self,number):
        
        if self.timing_flag == False :
            self.timing_seconds = 0
        self.st = 0
        self.ids.A2.text = ''
        answer=self.answer
        num=number
        if num != '' :
            if int(num)==int(answer): #注意这里answer是字符，不过不加int()会一直判定为假
                self.sta = self.sta + 1 
            else:
                pass

        self.word='提交'
        self.sto=self.sto+1
        num_do=self.sto
        self.record='已做题目数量:'+str(num_do-1)
        self.word=self.word
        self.ids.x2.text = '点击蓝色开始，点此处结算'


    def restartscreen(self):

        self.endtime = ''
        self.st = self.st + 1
        self.ids.x2.text = '返回主页'
        self.ids.text_update.text = '一共做了 '+str(self.sto-1)+'道题，对了'+str(self.sta)+'道题'
        if self.sto >= 10:           
            if float(self.sta)/float(self.sto-1) < 0.6 :
                self.ids.labelA.text = '太菜了！（￣へ￣）'
            if  0.6 < float(self.sta)/float(self.sto-1) <= 0.8 :
                self.ids.labelA.text = '再接再厉┐(￣ヮ￣)┌'
            if float(self.sta)/float(self.sto-1) > 0.8:
                self.ids.labelA.text = '厉害捏! (°Д°) '
        if self.sto < 10 :
            self.ids.labelA.text = '才做这点题就不想做了? (⊙_⊙)'
        if self.st >= 2:
            self.timing_seconds = 0
            self.ids.time.text = '00:00:00'
            self.manager.current = 'menu'
            self.word='提交'
            self.ids.x2.text = '点击蓝色开始，点此处结算'
            self.ids.text_update.text = '别卷了！求求你了！(ㄒoㄒ) '
            self.ids.labelA.text = '别卷了！求求你了！(ㄒoㄒ) '
        self.timing_flag = False
        self.word = '重新开始'
        self.sta = 0
        self.sto  = 0








    pass

class Multiplication_1Screen(Screen):


    record = StringProperty()
    asking = StringProperty()
    word = StringProperty()
    


    def __init__(self, **kwargs):
        super(Multiplication_1Screen, self).__init__(**kwargs)
        self.timing_flag = False
        self.timing_seconds = 0
        self.answer=0
        self.sto  = 0
        self.sta = 0
        self.st=0
        self.endtime = ''
        self.on_start()
 
    def on_start(self):
        # 设置clock 每0秒执行一次，代表实时进行不间断刷新。
        Clock.schedule_interval(self.update_time, 0)
 
    def update_time(self, nap):
        if self.timing_flag:
            self.timing_seconds += nap

        m, s = divmod(self.timing_seconds, 60)
        self.ids.time.text = ('%02d:%02d.[size=40]%02d[/size]' % (int(m), int(s), int(s * 100 % 100)))

    def start_on_stop(self):
        self.timing_flag = True
 

    def begin(self):
        self.a=random.randint(1,9)
        self.b=random.randint(1,9)
        self.answer=self.a*self.b
        asking=str(self.a)+'×'+str(self.b)+'='

        self.asking=asking


    def yorn(self,number):
        
        if self.timing_flag == False :
            self.timing_seconds = 0
        self.st = 0
        self.ids.A2.text = ''
        answer=self.answer
        num=number
        if num != '' :
            if int(num)==int(answer): #注意这里answer是字符，不过不加int()会一直判定为假
                self.sta = self.sta + 1 
            else:
                pass

        self.word='提交'
        self.sto=self.sto+1
        num_do=self.sto
        self.record='已做题目数量:'+str(num_do-1)
        self.word=self.word
        self.ids.x2.text = '点击蓝色开始，点此处结算'


    def restartscreen(self):

        self.endtime = ''
        self.st = self.st + 1
        self.ids.x2.text = '返回主页'
        self.ids.text_update.text = '一共做了 '+str(self.sto-1)+'道题，对了'+str(self.sta)+'道题'
        if self.sto >= 10:           
            if float(self.sta)/float(self.sto-1) < 0.6 :
                self.ids.labelA.text = '太菜了！（￣へ￣）'
            if  0.6 < float(self.sta)/float(self.sto-1) <= 0.8 :
                self.ids.labelA.text = '再接再厉┐(￣ヮ￣)┌'
            if float(self.sta)/float(self.sto-1) > 0.8:
                self.ids.labelA.text = '厉害捏! (°Д°) '
        if self.sto < 10 :
            self.ids.labelA.text = '才做这点题就不想做了? (⊙_⊙)'
        if self.st >= 2:
            self.timing_seconds = 0
            self.ids.time.text = '00:00:00'
            self.manager.current = 'menu'
            self.word='提交'
            self.ids.x2.text = '点击蓝色开始，点此处结算'
            self.ids.text_update.text = '别卷了！求求你了！(ㄒoㄒ) '
            self.ids.labelA.text = '别卷了！求求你了！(ㄒoㄒ) '
        self.timing_flag = False
        self.word = '重新开始'
        self.sta = 0
        self.sto  = 0








    pass

class Multiplication_2Screen(Screen):


    record = StringProperty()
    asking = StringProperty()
    word = StringProperty()
    


    def __init__(self, **kwargs):
        super(Multiplication_2Screen, self).__init__(**kwargs)
        self.timing_flag = False
        self.timing_seconds = 0
        self.answer=0
        self.sto  = 0
        self.sta = 0
        self.st=0
        self.endtime = ''
        self.on_start()
 
    def on_start(self):
        # 设置clock 每0秒执行一次，代表实时进行不间断刷新。
        Clock.schedule_interval(self.update_time, 0)
 
    def update_time(self, nap):
        if self.timing_flag:
            self.timing_seconds += nap

        m, s = divmod(self.timing_seconds, 60)
        self.ids.time.text = ('%02d:%02d.[size=40]%02d[/size]' % (int(m), int(s), int(s * 100 % 100)))

    def start_on_stop(self):
        self.timing_flag = True
 

    def begin(self):
        self.a=random.randint(1,9)
        self.b=random.randint(10,99)
        self.answer=self.a*self.b
        asking=str(self.a)+'×'+str(self.b)+'='

        self.asking=asking


    def yorn(self,number):
        
        if self.timing_flag == False :
            self.timing_seconds = 0
        self.st = 0
        self.ids.A2.text = ''
        answer=self.answer
        num=number
        if num != '' :
            if int(num)==int(answer): #注意这里answer是字符，不过不加int()会一直判定为假
                self.sta = self.sta + 1 
            else:
                pass

        self.word='提交'
        self.sto=self.sto+1
        num_do=self.sto
        self.record='已做题目数量:'+str(num_do-1)
        self.word=self.word
        self.ids.x2.text = '点击蓝色开始，点此处结算'


    def restartscreen(self):

        self.endtime = ''
        self.st = self.st + 1
        self.ids.x2.text = '返回主页'
        self.ids.text_update.text = '一共做了 '+str(self.sto-1)+'道题，对了'+str(self.sta)+'道题'
        if self.sto >= 10:           
            if float(self.sta)/float(self.sto-1) < 0.6 :
                self.ids.labelA.text = '太菜了！（￣へ￣）'
            if  0.6 < float(self.sta)/float(self.sto-1) <= 0.8 :
                self.ids.labelA.text = '再接再厉┐(￣ヮ￣)┌'
            if float(self.sta)/float(self.sto-1) > 0.8:
                self.ids.labelA.text = '厉害捏! (°Д°) '
        if self.sto < 10 :
            self.ids.labelA.text = '才做这点题就不想做了? (⊙_⊙)'
        if self.st >= 2:
            self.timing_seconds = 0
            self.ids.time.text = '00:00:00'
            self.manager.current = 'menu'
            self.word='提交'
            self.ids.x2.text = '点击蓝色开始，点此处结算'
            self.ids.text_update.text = '别卷了！求求你了！(ㄒoㄒ) '
            self.ids.labelA.text = '别卷了！求求你了！(ㄒoㄒ) '
        self.timing_flag = False
        self.word = '重新开始'
        self.sta = 0
        self.sto  = 0








    pass

class Multiplication_3Screen(Screen):


    record = StringProperty()
    asking = StringProperty()
    word = StringProperty()
    


    def __init__(self, **kwargs):
        super(Multiplication_3Screen, self).__init__(**kwargs)
        self.timing_flag = False
        self.timing_seconds = 0
        self.answer=0
        self.sto  = 0
        self.sta = 0
        self.st=0
        self.endtime = ''
        self.on_start()
 
    def on_start(self):
        # 设置clock 每0秒执行一次，代表实时进行不间断刷新。
        Clock.schedule_interval(self.update_time, 0)
 
    def update_time(self, nap):
        if self.timing_flag:
            self.timing_seconds += nap

        m, s = divmod(self.timing_seconds, 60)
        self.ids.time.text = ('%02d:%02d.[size=40]%02d[/size]' % (int(m), int(s), int(s * 100 % 100)))

    def start_on_stop(self):
        self.timing_flag = True
 

    def begin(self):
        self.a=random.randint(10,99)
        self.b=random.randint(10,99)
        self.answer=self.a*self.b
        asking=str(self.a)+'×'+str(self.b)+'='

        self.asking=asking


    def yorn(self,number):
        
        if self.timing_flag == False :
            self.timing_seconds = 0
        self.st = 0
        self.ids.A2.text = ''
        answer=self.answer
        num=number
        if num != '' :
            if int(num)==int(answer): #注意这里answer是字符，不过不加int()会一直判定为假
                self.sta = self.sta + 1 
            else:
                pass

        self.word='提交'
        self.sto=self.sto+1
        num_do=self.sto
        self.record='已做题目数量:'+str(num_do-1)
        self.word=self.word
        self.ids.x2.text = '点击蓝色开始，点此处结算'


    def restartscreen(self):

        self.endtime = ''
        self.st = self.st + 1
        self.ids.x2.text = '返回主页'
        self.ids.text_update.text = '一共做了 '+str(self.sto-1)+'道题，对了'+str(self.sta)+'道题'
        if self.sto >= 10:           
            if float(self.sta)/float(self.sto-1) < 0.6 :
                self.ids.labelA.text = '太菜了！（￣へ￣）'
            if  0.6 < float(self.sta)/float(self.sto-1) <= 0.8 :
                self.ids.labelA.text = '再接再厉┐(￣ヮ￣)┌'
            if float(self.sta)/float(self.sto-1) > 0.8:
                self.ids.labelA.text = '厉害捏! (°Д°) '
        if self.sto < 10 :
            self.ids.labelA.text = '才做这点题就不想做了? (⊙_⊙)'
        if self.st >= 2:
            self.timing_seconds = 0
            self.ids.time.text = '00:00:00'
            self.manager.current = 'menu'
            self.word='提交'
            self.ids.x2.text = '点击蓝色开始，点此处结算'
            self.ids.text_update.text = '别卷了！求求你了！(ㄒoㄒ) '
            self.ids.labelA.text = '别卷了！求求你了！(ㄒoㄒ) '
        self.timing_flag = False
        self.word = '重新开始'
        self.sta = 0
        self.sto  = 0








    pass

class Division_1Screen(Screen):


    record = StringProperty()
    asking = StringProperty()
    word = StringProperty()
    


    def __init__(self, **kwargs):
        super(Division_1Screen, self).__init__(**kwargs)
        self.timing_flag = False
        self.timing_seconds = 0
        self.answer=0
        self.sto  = 0
        self.sta = 0
        self.st=0
        self.endtime = ''
        self.on_start()
 
    def on_start(self):
        # 设置clock 每0秒执行一次，代表实时进行不间断刷新。
        Clock.schedule_interval(self.update_time, 0)
 
    def update_time(self, nap):
        if self.timing_flag:
            self.timing_seconds += nap

        m, s = divmod(self.timing_seconds, 60)
        self.ids.time.text = ('%02d:%02d.[size=40]%02d[/size]' % (int(m), int(s), int(s * 100 % 100)))

    def start_on_stop(self):
        self.timing_flag = True
 

    def begin(self):
        self.a=random.randint(1,9)
        self.b=random.randint(1,9)
        self.answer=self.a*self.b
        asking=str(self.answer)+'÷'+str(self.a)+'='

        self.asking=asking


    def yorn(self,number):
        
        if self.timing_flag == False :
            self.timing_seconds = 0
        self.st = 0
        self.ids.A2.text = ''
        answer=self.answer
        num=number
        if num != '' :
            if int(num)*int(self.a) == self.answer : #注意这里answer是字符，不过不加int()会一直判定为假
                self.sta = self.sta + 1 
            else:
                pass

        self.word='提交'
        self.sto=self.sto+1
        num_do=self.sto
        self.record='已做题目数量:'+str(num_do-1)
        self.word=self.word
        self.ids.x2.text = '点击蓝色开始，点此处结算'


    def restartscreen(self):

        self.endtime = ''
        self.st = self.st + 1
        self.ids.x2.text = '返回主页'
        self.ids.text_update.text = '一共做了 '+str(self.sto-1)+'道题，对了'+str(self.sta)+'道题'
        if self.sto >= 10:           
            if float(self.sta)/float(self.sto-1) < 0.6 :
                self.ids.labelA.text = '太菜了！（￣へ￣）'
            if  0.6 < float(self.sta)/float(self.sto-1) <= 0.8 :
                self.ids.labelA.text = '再接再厉┐(￣ヮ￣)┌'
            if float(self.sta)/float(self.sto-1) > 0.8:
                self.ids.labelA.text = '厉害捏! (°Д°) '
        if self.sto < 10 :
            self.ids.labelA.text = '才做这点题就不想做了? (⊙_⊙)'
        if self.st >= 2:
            self.timing_seconds = 0
            self.ids.time.text = '00:00:00'
            self.manager.current = 'menu'
            self.word='提交'
            self.ids.x2.text = '点击蓝色开始，点此处结算'
            self.ids.text_update.text = '别卷了！求求你了！(ㄒoㄒ) '
            self.ids.labelA.text = '别卷了！求求你了！(ㄒoㄒ) '
        self.timing_flag = False
        self.word = '重新开始'
        self.sta = 0
        self.sto  = 0








    pass

class Division_2Screen(Screen):


    record = StringProperty()
    asking = StringProperty()
    word = StringProperty()
    


    def __init__(self, **kwargs):
        super(Division_2Screen, self).__init__(**kwargs)
        self.timing_flag = False
        self.timing_seconds = 0
        self.answer=0
        self.sto  = 0
        self.sta = 0
        self.st=0
        self.endtime = ''
        self.on_start()
 
    def on_start(self):
        # 设置clock 每0秒执行一次，代表实时进行不间断刷新。
        Clock.schedule_interval(self.update_time, 0)
 
    def update_time(self, nap):
        if self.timing_flag:
            self.timing_seconds += nap

        m, s = divmod(self.timing_seconds, 60)
        self.ids.time.text = ('%02d:%02d.[size=40]%02d[/size]' % (int(m), int(s), int(s * 100 % 100)))

    def start_on_stop(self):
        self.timing_flag = True
 

    def begin(self):
        self.a=random.randint(1,99)
        self.b=random.randint(1,10)
        self.answer=self.a*self.b
        asking=str(self.answer)+'÷'+str(self.a)+'='

        self.asking=asking


    def yorn(self,number):
        
        if self.timing_flag == False :
            self.timing_seconds = 0
        self.st = 0
        self.ids.A2.text = ''
        answer=self.answer
        num=number
        if num != '' :
            if int(num)*int(self.a) == self.answer : #注意这里answer是字符，不过不加int()会一直判定为假
                self.sta = self.sta + 1 
            else:
                pass

        self.word='提交'
        self.sto=self.sto+1
        num_do=self.sto
        self.record='已做题目数量:'+str(num_do-1)
        self.word=self.word
        self.ids.x2.text = '点击蓝色开始，点此处结算'


    def restartscreen(self):

        self.endtime = ''
        self.st = self.st + 1
        self.ids.x2.text = '返回主页'
        self.ids.text_update.text = '一共做了 '+str(self.sto-1)+'道题，对了'+str(self.sta)+'道题'
        if self.sto >= 10:           
            if float(self.sta)/float(self.sto-1) < 0.6 :
                self.ids.labelA.text = '太菜了！（￣へ￣）'
            if  0.6 < float(self.sta)/float(self.sto-1) <= 0.8 :
                self.ids.labelA.text = '再接再厉┐(￣ヮ￣)┌'
            if float(self.sta)/float(self.sto-1) > 0.8:
                self.ids.labelA.text = '厉害捏! (°Д°) '
        if self.sto < 10 :
            self.ids.labelA.text = '才做这点题就不想做了? (⊙_⊙)'
        if self.st >= 2:
            self.timing_seconds = 0
            self.ids.time.text = '00:00:00'
            self.manager.current = 'menu'
            self.word='提交'
            self.ids.x2.text = '点击蓝色开始，点此处结算'
            self.ids.text_update.text = '别卷了！求求你了！(ㄒoㄒ) '
            self.ids.labelA.text = '别卷了！求求你了！(ㄒoㄒ) '
        self.timing_flag = False
        self.word = '重新开始'
        self.sta = 0
        self.sto  = 0








    pass

class Division_3Screen(Screen):


    record = StringProperty()
    asking = StringProperty()
    word = StringProperty()
    


    def __init__(self, **kwargs):
        super(Division_3Screen, self).__init__(**kwargs)
        self.timing_flag = False
        self.timing_seconds = 0
        self.answer=0
        self.sto  = 0
        self.sta = 0
        self.st=0
        self.endtime = ''
        self.on_start()
 
    def on_start(self):
        # 设置clock 每0秒执行一次，代表实时进行不间断刷新。
        Clock.schedule_interval(self.update_time, 0)
 
    def update_time(self, nap):
        if self.timing_flag:
            self.timing_seconds += nap

        m, s = divmod(self.timing_seconds, 60)
        self.ids.time.text = ('%02d:%02d.[size=40]%02d[/size]' % (int(m), int(s), int(s * 100 % 100)))

    def start_on_stop(self):
        self.timing_flag = True
 

    def begin(self):
        self.a=random.randint(100,500)
        self.b=random.randint(10,99)
        self.answer=self.a*self.b
        asking=str(self.answer)+'÷'+str(self.a)+'='

        self.asking=asking


    def yorn(self,number):
        
        if self.timing_flag == False :
            self.timing_seconds = 0
        self.st = 0
        self.ids.A2.text = ''
        answer=self.answer
        num=number
        if num != '' :
            if int(num)*int(self.a) == self.answer : #注意这里answer是字符，不过不加int()会一直判定为假
                self.sta = self.sta + 1 
            else:
                pass

        self.word='提交'
        self.sto=self.sto+1
        num_do=self.sto
        self.record='已做题目数量:'+str(num_do-1)
        self.word=self.word
        self.ids.x2.text = '点击蓝色开始，点此处结算'


    def restartscreen(self):

        self.endtime = ''
        self.st = self.st + 1
        self.ids.x2.text = '返回主页'
        self.ids.text_update.text = '一共做了 '+str(self.sto-1)+'道题，对了'+str(self.sta)+'道题'
        if self.sto >= 10:           
            if float(self.sta)/float(self.sto-1) < 0.6 :
                self.ids.labelA.text = '太菜了！（￣へ￣）'
            if  0.6 < float(self.sta)/float(self.sto-1) <= 0.8 :
                self.ids.labelA.text = '再接再厉┐(￣ヮ￣)┌'
            if float(self.sta)/float(self.sto-1) > 0.8:
                self.ids.labelA.text = '厉害捏! (°Д°) '
        if self.sto < 10 :
            self.ids.labelA.text = '才做这点题就不想做了? (⊙_⊙)'
        if self.st >= 2:
            self.timing_seconds = 0
            self.ids.time.text = '00:00:00'
            self.manager.current = 'menu'
            self.word='提交'
            self.ids.x2.text = '点击蓝色开始，点此处结算'
            self.ids.text_update.text = '别卷了！求求你了！(ㄒoㄒ) '
            self.ids.labelA.text = '别卷了！求求你了！(ㄒoㄒ) '
        self.timing_flag = False
        self.word = '重新开始'
        self.sta = 0
        self.sto  = 0








    pass

class ct(App):
    def build(self):
        sm=ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(AdditionScreen(name='Addition'))
        sm.add_widget(SubtractionScreen(name='Subtraction'))
        sm.add_widget(MultiplicationScreen(name='Multiplication'))
        sm.add_widget(DivisionScreen(name='Division'))
        sm.add_widget(Addition1Screen(name='A1'))
        sm.add_widget(Addition2Screen(name='A2'))
        sm.add_widget(Addition3Screen(name='A3'))
        sm.add_widget(Subtraction1Screen(name='S1'))
        sm.add_widget(Subtraction2Screen(name='S2'))
        sm.add_widget(Subtraction3Screen(name='S3'))
        sm.add_widget(Multiplication_1Screen(name='M1'))
        sm.add_widget(Multiplication_2Screen(name='M2'))
        sm.add_widget(Multiplication_3Screen(name='M3'))
        sm.add_widget(Division_1Screen(name='D1'))
        sm.add_widget(Division_2Screen(name='D2'))
        sm.add_widget(Division_3Screen(name='D3'))
        sm.add_widget(LogScreen(name='LS'))


        return sm

if __name__ == '__main__':
    ct().run()


     
#coding:utf8

#初始化程序
from chromeclick import click as run, msgbox

msgbox(u'请等待，程序正在启动！',u'启动中')

from tkinter import *
from threading import Thread
import thread
import os
import time
import argparse

''''#重新启动Chrome
parser = argparse.ArgumentParser(description='This argparse is ued to RESTARTING.\
User do NOT need to use this.\
This program could be start by just CLICK TWICE!')
parser.add_argument('--keyword', type=str, default=None)
args = parser.parse_args()
if args.keyword != None:
    thread.start_new_thread(run, (args.keyword,))
    #exit()
else:
    del parser
    del args
    
time.sleep(2)'''

#初始化GUI界面
root = Tk()
root.geometry('500x314')
root.iconbitmap('favicon.ico')
root.title('百度点击模拟 Powered By MNS-QUC')

#初始化环境变量
var=StringVar()

#初始化GUI函数
def start():
    thread.start_new_thread(run, (var.get(),))

def peiyuanyuan():#(⊙o⊙)…发泄一下失恋情绪，忽略这个函数名字
    os.system("intro")

def intro(event):
    thread.start_new_thread(peiyuanyuan, ())

#初始化并部署GUI构件
textLabel = Label(root,text="使用前请先参阅说明进行设置(点击这里)",bg='#B0E0E6')
textLabel.place(x=137, y=0, anchor=NW)

textLabel2 = Label(root,text="输入网站关键词，然后点击开始，\n程序会弹出黑色弹窗并调用Chrome")
textLabel2.place(x=137, y=60, anchor=NW)

L1 = Label(root, text="网站关键词\nKeywords of your site",font=("宋体",8))
L1.place(x=85, y=138, anchor=NW)

E1 = Entry(root, bd =5, textvariable=var)
E1.place(x=220, y=139, anchor=NW)

B = Button(root, text ="点击开始", command = start, font=("华文行楷",12))
B.place(x=220, y=239, anchor=NW)

L2 = Label(root, text="Copyright© 中国秦川联盟网络安全部版权所有\n© Ministry of Network Security Affiliated Qinchuan Union of China")#,font=("华文行楷",12))
L2.place(x=55, y=270, anchor=NW)

#绑定说明点击事件
textLabel.bind("<Button-1>", intro)

#开启GUI
root.mainloop()

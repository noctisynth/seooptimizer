#!/usr/bin/env python
#coding: utf-8

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
from selenium.webdriver.support.wait import WebDriverWait
import os
from win32api import MessageBox
import thread

def msg(text, title):
    MessageBox(0, text, title)

def msgbox(text, title):
    thread.start_new_thread(msg, (text, title,))
    
def click(keyword):
    try:
        browser = webdriver.Chrome()
    except selenium.common.exceptions.SessionNotCreatedException:
        msg(u"ChromeDriver版本与Chrome浏览器版本不一致！请参阅“intro.txt”获取信息，或向中国秦川联盟官方申请技术支持。",u"ChromeDriver错误")
        raise NameError("Chrome Driver Version Does Not Fit.")
    browser.get('http://www.baidu.com')
    browser.find_element_by_id('kw').send_keys(keyword)
    browser.implicitly_wait(10)
    browser.find_element_by_id('su').send_keys(Keys.ENTER)
    a = 0
    err = 0
    ti = 1
    while True:
        
        try:
            pre=[]
            ti = ti+1
            line_list = browser.find_elements_by_xpath("//h3[@class='t']")
            #print line_list
            c = 0
            for line in line_list:
                c=c+1
                t = line.find_element_by_xpath('a')
                if pre=="":
                    pre[c] = t.text
                else:
                    for i in pre:
                        if i == t.text:
                            browser.quit()
                            os.system('restart --keyword %d'%keyword)
                            
                if u'中国秦川联盟' in t.text or keyword in t.text:
                    print '%s' % (t.text)
                    #print u'我方页面'
                    t.click()
                    time.sleep(3)
                    continue
                #else:
                    #print u'无效页面'
            line_list = browser.find_elements_by_xpath("//span[@class='pc']")
            page = 0
            for line in line_list:
                page = page + 1
                if page == ti:
                    line.click()
                    a = a + 1
                    #thread.start_new_thread(turnpage, (a, ti, ) )
                    print u"此时的页码：%s" % str(a)
                    print u"将要翻到的页码：%s" % str(ti)
                    print "\n"
                    #if a==3:
                      #  browser.quit()
                     #   break
                    time.sleep(1.5)
                    done = True
                    break
            
        except Exception, e:
            err = err+1
            if err == 10:
                try:
                    print u"[-]过多错误."
                    browser.quit()
                    #break
                except:
                    pass
                os.system('restart --keyword %d'%keyword)
                exit()
            print '[-]{}'.format(e)
            print 'Unable to click.'
            time.sleep(2)
    if done:
        print u"[*]执行到Done."
        try:
            browser.quit()
        except:
            pass
        os.system('restart --keyword %d'%keyword)
            
if __name__=="__main__":            
    while True:
        try:
            click(u"中国秦川联盟")
            time.sleep(5)
        except Exception, e:
            print '[-]Mistake:%s'%e
            time.sleep(2)

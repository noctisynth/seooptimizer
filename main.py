#!/usr/bin/env python
import time
import os

from loguru import logger
from DrissionPage import ChromiumPage
from DrissionPage import ChromiumOptions
from DrissionPage.common import Keys

DEBUG = False
co = ChromiumOptions()
co.auto_port(True)
if not DEBUG:
    co.set_argument("--headless")

def click(keyword: str, wait: int=5.5, turn_wait: int=2, depth: int=3):
    logger.info("主程序启动.")
    browser = ChromiumPage(addr_driver_opts=co)
    logger.info("浏览器控件设置完毕.")
    browser.get('http://www.baidu.com')
    logger.success("打开百度`https://www.baidu.com`.")
    browser.ele('#kw').input(keyword)
    browser.ele('#su').input(Keys.ENTER)
    logger.success(f"传入搜索关键词`{keyword}`.")

    err = 0
    page = 1
    clicked = []
    page_changed = False

    while True:
        try:
            content_left = browser.ele("#wrapper_wrapper").ele("#container").ele("#content_left")
            title_list = content_left.eles("tag:h3")

            for title in title_list:
                link = title.ele('tag:a')
                
                if link.text in clicked:
                    time.sleep(wait)
                    browser.quit()
                    return True
                clicked.append(link.attr("href"))
 
                if keyword in link.text:
                    link.click()
                    link_href = link.attr('href') if len(link.attr('href')) <= 55 else link.attr('href')[:55] + "..."
                    logger.success(f"点击链接: {link_href}")
            
            if page == depth:
                logger.info(f"已抵达预定的搜索深度: {depth}.")
                time.sleep(wait)
                browser.quit()
                return True

            page_links = browser.ele("#page").eles("tag:a")

            for page_link in page_links:
                if page_link.text == str(page+1):
                    page_link.click()
                    page += 1
                    page_changed = True
                    clicked = []
                    logger.info(f"翻页: {page}")
                    time.sleep(turn_wait)
                    break
                else:
                    page_changed = False

            if not page_changed:
                logger.info("已到搜索页面末页.")
                time.sleep(wait)
                browser.quit()
                return True
        except Exception as e:
            err += 1
            logger.error('无法自动点击页面:')
            logger.exception(e)
            if err == 10:
                logger.critical("错误次数超出预期.")
                try:
                    browser.quit()
                except:
                    pass
                return False
            time.sleep(wait)
            continue

def run(keyword, wait=5.5, turn_wait=2, depth=3):
    try:
        return click(keyword, wait=5.5, turn_wait=2, depth=3)
    except Exception as e:
        logger.exception(e)
        time.sleep(5.5)

def main(keyword, loop=False):
    while True:
        if run(keyword, wait=5.5, turn_wait=2, depth=3) and not loop:
            break
        
if __name__=="__main__":            
    main("百度贴吧")

# -*- coding: cp936 -*-

from chromeclick import click as run, msgbox
import argparse
import threading
import time

#重启Chrome
parser = argparse.ArgumentParser(description='This argparse is ued to RESTARTING.\
User do NOT need to use this.\
This program could be start by just CLICK TWICE!')
parser.add_argument('--keyword', type=str, default=None)
args = parser.parse_args()
if args.keyword != None:
    start = threading.Thread(target=run,args=(args.keyword,))
    start.start()
else:
    print "What's the fuck you are doing?"
    time.sleep(2)
    exit()

start.join()

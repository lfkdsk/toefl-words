#!/usr/bin/python
#coding=utf-8

# 依赖
# MacFSEvents           http://pypi.python.org/pypi/MacFSEvents/0.2.1

# -d 需要监控的文件夹路径
# -a 监控到事件后需要执行的命令
# -m 提醒内容

import os, sys, time
from fsevents import Observer, Stream

def main():
    is_starting = False
    more_action = False
    
    def callback(fileEvent):
        more_action = True
        if is_starting:
            return
        else:
            do_action()

    def do_action():
        is_starting = True
        more_action = False
        os.system('git add -A')
        os.system('git commit -m \" update by watch system \" ')
        print time.strftime('%H:%M:%S', time.localtime(time.time()))
        print '----------------------------------------------------'
        time.sleep(2)
        if (more_action):
            do_action()
        else:
            is_starting = False

    observer = Observer()
    stream = Stream(callback, '.', file_events=True)
    observer.schedule(stream)
    observer.start()

if __name__ == '__main__':
    main()

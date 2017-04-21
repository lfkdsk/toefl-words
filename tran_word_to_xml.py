# -*- coding: utf-8 -*-
import os
import sys
import time
from xml.dom.minidom import Document

def read_file(file_name):
    for line in open(file_name):
        if '##' not in line and '----' not in line and line.startswith('|'):
            temp = line.replace(' ', '')
            if not temp.startswith('||||'):
                parser_line(line[1:].lstrip().rstrip())
    pass

def check_invalid(file_name):
    file = open(file_name, 'r')
    first_line = file.readline()
    file.close();
    if not first_line.startswith('# - used - '):
        read_file(file_name);
        pass

def parser_line(line):
    index = line.find('|')
    global last_item
    global word_dict
    if index > 0:
        word = line[:index]
        if not line.startswith('Word') and not line.startswith('word'):               
            word_item = [word, line[index:].replace('|',' ')]
            last_item = word_item
            word_dict.append(word_item)
    elif index == 0:
        last_item[1] += '\n' + line[index:].replace('|',' ')

# initial and read file
def initial_search():
    print sys.argv[1]
    check_invalid(sys.argv[1])

    contentText = ""
    doc = Document()  # 创建DOM文档对象
    word_book = doc.createElement('wordbook') # 创建根元素
    doc.appendChild(word_book)

    time_text = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    for word_item in word_dict:
        item = doc.createElement('item')
        word = doc.createElement('word')
        trans = doc.createElement('trans')
        tag = doc.createElement('tag')

        word.appendChild(doc.createTextNode(word_item[0]))
        trans.appendChild(doc.createTextNode(word_item[1].encode('utf-8')))
        tag.appendChild(doc.createTextNode(time_text))

        item.appendChild(word)
        item.appendChild(trans)
        item.appendChild(tag)
        word_book.appendChild(item)
        pass

    out_file = open('output/' + sys.argv[1].replace('.md', '_xml.xml'),'w')
    out_file.write(doc.toprettyxml(indent = ''))
    out_file.close()
       
    print '\033[1;31m'
    print 'word count : ' + str(len(word_dict))
    print 'output file success! xml file in ' + out_file.name
    print '\033[0m'

    pass

global word_dict

global last_item

word_dict = []
last_item = []

initial_search()


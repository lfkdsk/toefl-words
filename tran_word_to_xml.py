# -*- coding: utf-8 -*-
import os
import sys
import word_lib as lib
import time
from xml.dom.minidom import Document


# initial and read file
def initial_search():
    print sys.argv[1]
    lib.check_invalid(sys.argv[1])

    contentText = ""
    doc = Document()  # 创建DOM文档对象
    word_book = doc.createElement('wordbook') # 创建根元素
    doc.appendChild(word_book)

    time_text = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    for word_item in lib.word_dict:
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
    print 'word count : ' + str(len(lib.word_dict))
    print 'output file success! xml file in ' + out_file.name
    print '\033[0m'

    pass

initial_search()


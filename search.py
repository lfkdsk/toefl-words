# -*- coding: utf-8 -*-

import os
import sys
import word_lib as lib

# search element
def search_word():

    sys.stdout.write(">>>  ")
    sys.stdout.flush()    

    word = raw_input()
    word_list = []
    real_word = []

    if word == '':
        return
    elif word == 'fk-':
        exit()
    elif word == 'up-':
        os.system('./update.sh')
        return
    elif word == 're-':
        # re - index 
        initial_search()
        return
    elif word == 'cl-':
        os.system('clear')
        return        

    for word_item in lib.word_dict:
        if word_item[0] != None and word_item[0].startswith(word):
            word_list.append(word_item)
            if word_item[0].lstrip().rstrip() == word:
                real_word = word

    if len(real_word) != 0:
        print real_word
    else:
        print 'no real word'
    for item in word_list:
        # word
        print '\033[1;31m'
        print item[0]
        print '\033[0m'
        # expr
        print item[1].encode('utf-8')
        # block
        print '################################################'
    if len(real_word) != 0:
        os.system('say ' + real_word);
    return

# initial and read file
def initial_search():
    lib.word_dict = []
    lib.last_item = []
    file_list = lib.scan_files("./", None, ".md")[1:] # remove ReadMe.md
    lib.read_files(file_list)
    pass

initial_search()

print '\033[1;31m'
print '----------------------------------------'
print '------学习TOEFL! word-count:' + str(len(lib.word_dict)) +'--------'
print '----------------------------------------'
print '\033[0m'

while True:
    search_word()

# -*- coding: utf-8 -*-

import os
import sys

def scan_files(directory, prefix=None, postfix=None):
    files_list = []

    for root, sub_dirs, files in os.walk(directory):
        for special_file in files:
            if postfix:
                if special_file.endswith(postfix):
                    files_list.append(os.path.join(root, special_file))
            elif prefix:
                if special_file.startswith(prefix):
                    files_list.append(os.path.join(root, special_file))
            else:
                files_list.append(os.path.join(root, special_file))

    return files_list


def read_files(directory_list):
    for file_name in directory_list:
        for line in open(file_name):
            if '##' not in line and '----' not in line and line.startswith('|'):
                line = line.replace(' ', '')
                if not line.startswith('||||'):
                    parser_line(line[1:])
        pass


def parser_line(line):
    index = line.find('|')
    global last_item
    if index > 0:
        word = line[:index]
        if not line.startswith('Word'):               
            word_item = [word, line[index:].replace('|',' ')]
            last_item = word_item
            word_dict.append(word_item)
    elif index == 0:
        last_item[1] += '\n' + line[index:].replace('|',' ')

def search_word():

    sys.stdout.write(">>>  ")
    sys.stdout.flush()    

    word = raw_input()
    word_list = []
    real_word = []

    if word == '':
        return
    elif word == 'fk':
        exit()
    elif word == 'up-':
        os.system('./update.sh')

    for word_item in word_dict:
        if word_item[0] != None and word_item[0].startswith(word):
            word_list.append(word_item)
            if word_item[0] == word:
                real_word = word

    if len(real_word) != 0:
        print real_word
    else:
        print 'no real word'
    for item in word_list:
        print item[0]
        print item[1].encode('utf-8')
        print '################################################'
    return

global word_dict

global last_item

word_dict = []
last_item = []

file_list = scan_files("./", None, ".md")[1:]

read_files(file_list)

while True:
    search_word()

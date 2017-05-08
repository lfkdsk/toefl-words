# -*- coding: utf-8 -*-

import os
import sys

global word_dict
global last_item
word_dict = []
last_item = []


# search file
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

# read files and parser
def read_files(directory_list):
    for file_name in directory_list:
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
        read_files([file_name]);
        pass


# parser every line
def parser_line(line):
    index = line.find('|')
    global last_item
    if index > 0:
        word = line[:index]
        if not line.startswith('Word') and not line.startswith('word'):               
            word_item = [word, line[index:].replace('|',' ')]
            last_item = word_item
            word_dict.append(word_item)
    elif index == 0:
        last_item[1] += '\n' + line[index:].replace('|',' ')




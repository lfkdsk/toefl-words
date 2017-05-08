# -*- coding: utf-8 -*-

from tran_word_to_xml import check_invalid, word_dict
import os
import sys

# initial and read file
def initial_spell():
    print sys.argv[1]
    check_invalid(sys.argv[1])
    for word_item in word_dict:
        print '\033[1;31m'
        print word_item[0]
        print '\033[0m'
        os.system('say ' + word_item[0])
        raw_input()
        print word_item[1].encode('utf-8')


initial_spell()
# -*- coding: utf-8 -*-

import os
import sys
import word_lib as lib

# initial and test spell 
def initial_spell():
    print sys.argv[1]
    lib.check_invalid(sys.argv[1])
    for word_item in lib.word_dict:
        print '\033[1;31m'
        print word_item[0]
        print '\033[0m'
        os.system('say ' + word_item[0])
        raw_input()
        print word_item[1].encode('utf-8')

initial_spell()
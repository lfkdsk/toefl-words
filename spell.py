# -*- coding: utf-8 -*-

import os
import sys
import word_lib as lib

# initial and test spell 
def initial_spell():
    print sys.argv[1]

    if sys.argv[1] == 'all':
        file_list = lib.scan_files("./", None, ".md")[1:] # remove ReadMe.md
        lib.read_files(file_list)
    else:
        lib.check_invalid(sys.argv[1])

    print str(len(lib.word_dict)) + ' words'

    jumpIndex = 0
    shouldJump = False

    if len(sys.argv) == 3:
        for item in lib.word_dict:
            if str(item[0].lstrip().rstrip()) == str(sys.argv[2]):
                shouldJump = True
                break                
            jumpIndex += 1

    if not shouldJump:
        jumpIndex = 0

    print shouldJump

    for word_item in lib.word_dict[jumpIndex:]:
        print '\033[1;31m'
        print word_item[0]
        print '\033[0m'
        os.system('say ' + word_item[0])
        raw_input()
        print word_item[1].encode('utf-8')

initial_spell()
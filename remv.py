#!/usr/bin/env python

import readline
import re
import shutil
import os
import sys

def raw_input_with_default(prompt, default):
    def pre_input_hook():
        readline.insert_text(default)
        readline.redisplay()
    
    readline.set_pre_input_hook(pre_input_hook)
    try:
        return raw_input(prompt)
    except KeyboardInterrupt:
        sys.exit()
    finally:
        readline.set_pre_input_hook(None)


def do_rename(files):
    all_good = False
    regex = None
    replacement = None
    while not all_good:
        regex = raw_input_with_default("Regex: ", regex)
        replacement = raw_input_with_default("Replacement: ",replacement)
        for f in files:
            print "`%s' -> `%s'" % (f, re.sub(regex, replacement, f))
            
        try:
            all_good = raw_input("All Good? [Y/n]:") in "Yy"
        except KeyboardInterrupt:
            sys.exit()

    for f in files:
        shutil.move(f, re.sub(regex, replacement, f))
    

if __name__ == "__main__":
    do_rename(sys.argv[1:])

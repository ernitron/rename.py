#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File: rename.py
# Author: ernitron (c) 2017
# Mit License

import os
import sys
import re

Version = "1.1.5"

# To print colored text on term
RED   = '\033[1;31m'
BLUE  = '\033[1;34m'
CYAN  = '\033[1;36m'
GREEN = '\033[0;32m'
RESET = '\033[0;0m'
BOLD  = '\033[;1m'
REV   = '\033[;7m'

def nocolor():
    global RED, BLUE, CYAN, GREEN, RESET, BOLD, REV
    RED   = ''
    BLUE  = ''
    CYAN  = ''
    GREEN = ''
    RESET = ''
    BOLD  = ''
    REV   = ''

def camel_case(fname):
    '''Convert to camel case: returns newname'''
    oldname = fname.replace('_', ' ')
    modified_name = re.findall('[\w]+', oldname.lower())
    return ''.join([word.title() for word in modified_name])

def replace_space(fname, fill_char='_'):
    '''Replace spaces with fill_char: fill_char: default to '_' :returns newname '''
    return fname.replace(' ', fill_char)

def replace_content(fname, contains=None, replace=None):
    if contains and contains in fname:
        if not replace:
            replace = ''
            return fname.replace(contains, replace)
    return fname

def lower_case(fname):
    '''Lower filename :returns newname '''
    return fname.lower()

def upper_case(fname):
    '''Upper filename :returns newname '''
    return fname.upper()

def skip_name(fname, skip=None):
    '''Skip in filename: returns: newname '''
    startlen = 0
    if skip and skip.isdigit():
        startlen += int(skip)
    # Initialize newname
    return fname[startlen:]

def start_name(fname, start=None):
    '''Skip start in filename: returns: newname '''
    startlen = 0
    if start and fname.startswith(start):
        startlen += len(start)
    # Initialize newname
    return fname[startlen:]

def add_number(fname, counter):
     return '%02d-%s' % (counter, fname)

def add_endnum(fname, counter):
     return '%s-%02d' % (fname, counter)

def substitute(fname, pattern, sub):
    if not pattern: return fname
    try:
        spb = pattern.split('/')
        return re.sub(spb[1], spb[2], fname)
    except:
        pass
    return re.sub(pattern, sub, fname)

def renaming(a):
    counter = 1
    endcounter = 1
    for filename in os.listdir():
        newname, extension = os.path.splitext(filename)
        extension = extension.lower()

        if a.match:
            if not re.match(a.match, filename):
                continue

        if a.suffix and not a.suffix in extension:
            continue
        if a.contains and not a.contains in filename:
            continue
        if a.verbose:
            print(CYAN, filename, RESET)

        if a.skip:
            newname = skip_name(newname, a.skip)
        if a.start:
            newname = start_name(newname, a.start)
        if a.contains and a.replace:
            newname = replace_content(newname, a.contains, a.replace)
        if a.pattern:
            newname = substitute(newname, a.pattern, a.replace)
        if a.camel:
            newname = camel_case(newname)
        if a.upper:
            newname = upper_case(newname)
        if a.lower:
            newname = lower_case(newname)
        if a.space:
            newname = replace_space(newname)
        if a.number:
            newname = add_number(newname, counter)
            counter += 1
        if a.endnum:
            newname = add_endnum(newname, counter)
            endcounter += 1

        newname = newname + extension

        do_rename(filename, newname, a.force)

def do_rename(oldname, newname, force):
    if oldname == newname or not newname :
        print('Nothing to change for ', RED, oldname, RESET)
        return
    if newname and force:
        try:
            os.rename(oldname, newname)
        except:
            print('Cannot rename ', RED, oldname, RESET)
            return
    print(oldname, '\n\t=>', GREEN, newname, RESET)

if __name__ == '__main__':
    import argparse

    example_text = '''Examples:
 rename.py --start start_of_file --skip 5 --contains This --replace That --number --suffix .mp3 --force
 would rename a file like: start_of_file1234_Take_This.mp3
                     into: 01-Take_That.mp3

 rename.py -s start_of_file -p '/This/That/' -k 5 -n -x mp3 -f
 rename.py -s start_of_file -p This -b That -k 5 -n -x mp3 -f
 would do the same
 '''

    parser = argparse.ArgumentParser(description='rename files', epilog=example_text,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('--root', default='./')
    parser.add_argument('-c', '--contains', help='check for string in filename; works with -r', default=None)
    parser.add_argument('-p', '--pattern', help='pattern with regex', default=None)
    parser.add_argument('-r', '--replace', help='replace for match string; works with -c and -p', default=None)
    parser.add_argument('-k', '--skip', help='skip this number of char from file', default=None)
    parser.add_argument('-m', '--match', help='apply only to file that match pattern', default=None)
    parser.add_argument('-s', '--start', help='replace start of filename', default=None)
    parser.add_argument('-x', '--suffix', help='apply only file with suffix like .mp3', default=None)
    # Bool
    parser.add_argument('-a', '--space', action='store_true', help='no space or replace space', default=False)
    parser.add_argument('-e', '--endnum', action='store_true', help='add a 2 digit sequence end of filename', default=False)
    parser.add_argument('-f', '--force', action='store_true', help='force to rename otherwise it just print', default=False)
    parser.add_argument('-n', '--number', action='store_true', help='add a 2 digit sequence start of filename', default=False)
    parser.add_argument('-u', '--upper', action='store_true', help='To upper', default=False)
    parser.add_argument('-l', '--lower', action='store_true', help='To lower', default=False)
    parser.add_argument('-R', '--recursive', action='store_true', help='Recursive', default=False)
    parser.add_argument('-C', '--camel', action='store_true', help='CamelCase', default=False)
    parser.add_argument('-v', '--verbose', action='store_true', help='verbose output', default=False)
    parser.add_argument('-V', '--version', action='store_true', help='print version', default=False)
    parser.add_argument('-L', '--nocolor', action='store_true', help='print version', default=False)

    # get args
    args = parser.parse_args()
    if not any([args.start, args.space, args.contains, args.replace, args.skip, args.force, args.pattern, args.sub, args.lower, args.upper, args.camel, args.verbose]):
        print("Version ", Version)
        parser.print_help()
        print("Sorry but I have nothing to do, did you try with some flags?\n\n")
        sys.exit(0)

    if args.version:
        print("Version ", Version)
        sys.exit(0)

    # If it is piped to other program (i.e. rename.py... | less) than don't color print!
    if not os.isatty(1) or args.nocolor:
        nocolor()

    # Where to start, what to get
    os.chdir(args.root)

    if args.recursive:
        for top, subdirs, files in os.walk(args.root):
            for d in subdirs:
                newdir = os.path.join(top, d)
                os.chdir(newdir)
                renaming(args)
    else:
        renaming(args)

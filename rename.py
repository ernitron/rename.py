#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File: rename.py
# Author: ernitron (c) 2017
# Mit License

import os
import sys
import re

Version = "1.1.7"

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

def skip_name(fname, skip=None):
    '''Skip first chars in filename: returns: newname '''
    startlen = 0
    if skip and skip.isdigit():
        startlen = int(skip)

def start_name(fname, start=None, replace=None):
    '''Skip string in filename: returns: newname '''
    if start and fname.startswith(start):
        startlen = len(skip)
        if not replace: replace = ''
        return replace + fname[startlen:]
    return fname

def camel_case(fname):
    '''Convert to CamelCase: returns newname'''
    tmpname = fname.replace('_', ' ')
    modified_name = re.findall('[\w]+', tmpname.lower())
    return ''.join([word.title() for word in modified_name])

def replace_space(fname, fill_char='_'):
    '''Replace spaces with fill_char: fill_char: default to '_' :returns newname '''
    return fname.replace(' ', fill_char)

def replace_content(fname, contains=None, replace=None):
    '''Replace content with replace string :returns newname '''
    if contains and contains in fname:
        if not replace:
            replace = ''
            return fname.replace(contains, replace)
    else: return fname

def lower_case(fname):
    '''Lower filename :returns newname '''
    return fname.lower()

def upper_case(fname):
    '''Upper filename :returns newname '''
    return fname.upper()

def add_number(fname, counter):
    '''Add a sequence 2digit at beginning of filename :returns newname '''
    return '%02d-%s' % (counter, fname)

def add_endnum(fname, counter):
    '''Add a sequence 2digit at end of filename :returns newname '''
    return '%s-%02d' % (fname, counter)

def substitute(fname, pattern, sub):
    if not pattern: return fname
    try:
        spb = pattern.split('/')
        return re.sub(spb[1], spb[2], fname)
    except:
        pass
    return re.sub(pattern, sub, fname)

def timestamp_name(fname, newname, pos='init'):
    from time import localtime, strftime
    filestat = os.stat(fname)
    timestring = strftime("%Y-%m-%d-%H:%M:%S", localtime(filestat.st_mtime))
    if pos == 'init':
        return f'{timestring}-{newname}'
    else:
        return f'{newname}-{timestring}'

def renaming(a):
    '''The loop on current dir to rename files based on requests'''

    # initialize counter
    try:
        startcounter = int(a.counter)
    except:
        startcounter = 1
    counter = startcounter
    endcounter = startcounter

    for filename in os.listdir():
        newname, extension = os.path.splitext(filename)
        extension = extension.lower()

        if a.directory and not os.path.isdir(filename): 
            continue
        if a.regular and not os.path.isfile(filename): 
            continue
        if a.match and not re.match(a.match, filename):
            continue
        if a.suffix and not a.suffix in extension:
            continue
        if a.contains and not a.contains in filename:
            continue
        if a.verbose:
            print('This is the file to do\t=>', CYAN, filename, RESET)

        if a.start:
            newname = start_name(newname, a.start, a.replace)
        if a.skip:
            newname = skip_name(newname, a.skip)
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
        if a.timestamp:
            newname = timestamp_name(filename, newname)
        if a.number:
            newname = add_number(newname, counter)
            counter += 1
        if a.endnum:
            newname = add_endnum(newname, endcounter)
            endcounter += 1
        # Finally do the rename on file or directory
        newname = newname + extension
        do_rename(filename, newname, a.force, a.yes)

def do_rename(oldname, newname, force, yes):
    if oldname == newname or not newname:
        print('Nothing to change for ', RED, oldname, RESET)
        return

    if not yes:
       yes = (input(f'Rename to "{newname}" ? [y/n]') == 'y')
       
    print('THIS FILE         \t=>', CYAN, oldname, RESET)
    if newname and force and yes:
        try:
            os.rename(oldname, newname)
            print('HAS BEEN RENAMED TO\t=>', GREEN, newname, RESET)
            
        except:
            print('Cannot rename ', RED, oldname, RESET)
    else:
        print('WILL BE RENAMED TO\t=>', GREEN, newname, RESET)


if __name__ == '__main__':
    import argparse

    example_text = '''\tExamples:
\trename.py --skip start_of_file --skip 5 --contains This --replace That --number --suffix .mp3 --force
\twould rename a file like: start_of_file1234_Take_This.mp3
                     into: 01-Take_That.mp3

\trename.py -k start_of_file -p '/This/That/' -k 5 -n -x mp3 -f
\trename.py -k start_of_file -p This -r That -k 5 -n -x mp3 -f
\twould do the same
 '''

    parser = argparse.ArgumentParser(description='rename files', epilog=example_text,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('--root', help='this will be the root directory', default='./')
    parser.add_argument('-c', '--contains', help='check for string in filename; works with -r', default=None)
    parser.add_argument('-p', '--pattern', help='pattern with regex', default=None)
    parser.add_argument('-r', '--replace', help='replace for match string; works with -c and -p', default=None)
    parser.add_argument('-k', '--skip', help='skip this number of char from filename', default=None)
    parser.add_argument('-s', '--start', help='delete string from beginning of filename', default=None)
    parser.add_argument('-m', '--match', help='apply only to file that match pattern', default=None)
    parser.add_argument('-t', '--counter', help='initialize with some value the sequence', default="1")
    parser.add_argument('-x', '--suffix', help='apply only to file with suffix like .mp3', default=None)
    # Bool
    parser.add_argument('-f', '--force', action='store_true', help='Force to rename (actual do the rename)', default=False)
    parser.add_argument('-A', '--space', action='store_true', help='Replace space with _', default=False)
    parser.add_argument('-C', '--camel', action='store_true', help='Transform filename in CamelCase', default=False)
    parser.add_argument('-E', '--endnum', action='store_true', help='Add a 2 digit sequence end of filename', default=False)
    parser.add_argument('-N', '--number', action='store_true', help='Add a 2 digit sequence start of filename', default=False)
    parser.add_argument('-D', '--directory', action='store_true', help='Apply only to directory', default=False)
    parser.add_argument('-F', '--regular', action='store_true', help='Apply only to regular files', default=False)
    parser.add_argument('-U', '--upper', action='store_true', help='Transform filename into upper case', default=False)
    parser.add_argument('-L', '--lower', action='store_true', help='Transform filename into lower case', default=False)
    parser.add_argument('-R', '--recursive', action='store_true', help='Recursive into subdirs', default=False)
    parser.add_argument('-V', '--version', action='store_true', help='Print version and die', default=False)
    parser.add_argument('-O', '--nocolor', action='store_true', help='Print without color', default=False)
    parser.add_argument('-Y', '--yes', action='store_false', help='Confirm before rename [y/n]', default=True)
    parser.add_argument('-T', '--timestamp', action='store_true', help='prefix with timestamp of file access time', default=False)
    parser.add_argument('-v', '--verbose', action='store_true', help='verbose output', default=False)

    # get args
    args = parser.parse_args()

    if not any([args.start, args.skip, args.space, args.contains, args.replace, args.force, args.pattern, args.lower, args.upper, args.camel, args.number, args.endnum, args.verbose]):
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

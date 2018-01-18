#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# File: rename.py
# Author: ernitron (c) 2017
# Mit License

import os
import sys
import re

Version = "1.2.7"

# To print colored text on term
RED   = ''
BLUE  = ''
CYAN  = ''
GREEN = ''
RESET = ''
BOLD  = ''
REV   = ''

def color():
    global RED, BLUE, CYAN, GREEN, RESET, BOLD, REV
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

def skip_name(fname, skip):
    '''Skip first chars in filename: returns: newname '''
    try:
        startlen = int(skip)
    except:
        startlen = 0
    return fname[startlen:]

def start_name(fname, start, replace):
    '''Skip string in filename: returns: newname '''
    startlen = 0
    fnamelower = fname.lower()
    if start and fnamelower.startswith(start.lower()):
        startlen = len(start)
    return replace + fname[startlen:]

def space_case(fname):
    '''Convert to Name Surname: returns newname'''
    prec = ''
    newname = ''
    for char in fname:
        if char == '_':
            newname += ' '
            continue
        if prec.islower() and char.isupper() :
            newname += ' '
        newname += char
        prec = char
    return newname

def camel_case(fname):
    '''Convert to CamelCase: returns newname'''
    tmpname = fname.replace('_', ' ')

    prec = ''
    newword = ''
    for char in tmpname:
        if prec.islower() and char.isupper() :
            newword += ' '
        newword += char
        prec = char
    tmpname = newword

    modified_name = re.findall('[\w]+', tmpname.lower())
    return ''.join([word.title() + ' ' for word in modified_name])

def replace_space(fname, fill_char='_'):
    '''Replace spaces with fill_char: fill_char: default to '_' :returns newname '''
    return fname.replace(' ', fill_char)

def replace_content(fname, contains, replace):
    '''Replace content with replace string :returns newname '''
    if contains and contains in fname:
        return fname.replace(contains, replace)
    else: return fname

def lower_case(fname):
    '''Lower filename :returns newname'''
    return fname.lower()

def upper_case(fname):
    '''Upper filename :returns newname'''
    return fname.upper()

def add_number(fname, counter, bottom):
    '''Add a sequence 2digit at beginning of filename :returns newname '''
    if bottom:
        return '%s-%02d' % (fname, counter)
    else:
        return '%02d-%s' % (counter, fname)

def substitute(fname, pattern, replace):
    if not pattern: return fname
    if pattern[-1] == 'i':
        flags = re.IGNORECASE
    else:
        flags = 0
    try:
        spb = pattern.split('/')
        return re.sub(spb[1], spb[2], fname, flags=flags)
    except:
        pass
    return re.sub(pattern, replace, fname)

def timestamp_name(fname, newname, bottom):
    from time import localtime, strftime
    filestat = os.stat(fname)
    timestring = strftime("%Y-%m-%d", localtime(filestat.st_mtime))
    if bottom:
        return f'{newname}-{timestring}'
    else:
        return f'{timestring}-{newname}'

def strip_name(fname):
    return fname.strip(' -._\t\n\r')

def swap_name(fname, swap):
    '''Swap name like Alfa Beta Gamma -> GAMMA, Alfa, Beta'''
    '''Swap name like Alfa Beta-> BETA, Alfa'''

    parts = fname.split(swap)
    newname = parts[-1].upper()
    for part in parts[0:-2] :
        part = part.strip(',')
        newname += ', ' + part.title()
    return newname

def sanitize_name(fname):
    sanitize = """[]()%@"!#$^&*,:;></?{}'"""
    for char in sanitize:
        fname = fname.replace(char,"")
    return strip_name(fname)

def bulk_rename(a):
    '''The loop on current dir to rename files based on requests'''
    # initialize counter
    try:
        counter = int(a.number)
    except:
        counter = 1

    if a.files:
        filelist = a.files
    else:
        filelist = os.listdir()

    for filename in filelist:

        newname, extension = os.path.splitext(filename)
        if a.extlower:
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

        if a.start:
            newname = start_name(newname, a.start, a.replace)
        if a.skip:
            newname = skip_name(newname, a.skip)
        if a.contains:
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
            newname = replace_space(newname, fill_char=a.space)
        if a.sanitize:
            newname = sanitize_name(newname)
        if a.timestamp:
            newname = timestamp_name(filename, newname, a.bottom)
        if a.number:
            newname = add_number(newname, counter, a.bottom)
            counter += 1
        if a.strip:
            newname = strip_name(newname)
        if a.swap:
            newname = swap_name(newname, a.swap)
        if a.extension:
           extension = a.extension

        # Finally do the rename on file or directory
        if not newname:
            newname = 'ZZZ-TBD'
            newname = timestamp_name(filename, newname, True)

        newname = newname + extension
        do_rename(filename, newname, a.force, a.yes, a.verbose)

def do_rename(oldname, newname, force, yes, verbose):
    if verbose:
        print('File to be renamed\t=>', CYAN, oldname, RESET)

    if not newname or oldname == newname:
        if verbose:
            print('Nothing to do for\t=>', RED, oldname, RESET)
        return

    if not yes:
       yes = (input(f'Rename {oldname} to "{newname}" ? [y/n] ') == 'y')

    print('THIS FILE         \t=>', GREEN, oldname, RESET)
    if newname and force and yes:
        if os.path.isfile(newname):
            print('FILE EXISTS NO RENAME\t=>', RED, newname, RESET)
            return
        try:
            os.rename(oldname, newname)
            print('HAS BEEN RENAMED TO\t=>', GREEN, newname, RESET)

        except:
            print('Cannot rename ', RED, oldname, RESET)
    else:
        print('WILL BE RENAMED TO\t=>', CYAN, newname, RESET)

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
    parser.add_argument('-a', '--space', help='Replace space with _', nargs='?', const='_')
    parser.add_argument('-c', '--contains', help='check for string in filename; works with -r')
    parser.add_argument('-p', '--pattern', help='pattern with regex')
    parser.add_argument('-r', '--replace', help='replace string; works with -c and -p', default='')
    parser.add_argument('-k', '--skip', help='skip this number of char from filename')
    parser.add_argument('-s', '--start', help='delete string from beginning of filename')
    parser.add_argument('-n', '--number', help='Add a 2 digit sequence start of filename', nargs='?', const='1')
    parser.add_argument('-m', '--match', help='apply only to file that match pattern')
    parser.add_argument('-x', '--suffix', help='apply only to file with suffix like .mp3')
    parser.add_argument('-w', '--swap', help='swap names Alfa Beta->Beta Alfa', default=' ')
    parser.add_argument('-e', '--extension', help='change extension .mp3')
    parser.add_argument('-f', '--files', help='apply to list of files', nargs='*')
    # Bool
    parser.add_argument('-F', '--force', action='store_true', help='Force to rename (do it!)', default=False)
    parser.add_argument('-B', '--bottom', action='store_true', help='put sequence at end')
    parser.add_argument('-C', '--camel', action='store_true', help='Transform filename in CamelCase')
    parser.add_argument('-D', '--directory', action='store_true', help='Apply only to directory')
    parser.add_argument('-G', '--regular', action='store_true', help='Apply only to regular files')
    parser.add_argument('-L', '--lower', action='store_true', help='Transform filename into lower case')
    parser.add_argument('-E', '--extlower', action='store_true', help='Transform extension into lower case')
    parser.add_argument('-U', '--upper', action='store_true', help='Transform filename into upper case')
    parser.add_argument('-R', '--recursive', action='store_true', help='Recursive into subdirs')
    parser.add_argument('-V', '--version', action='store_true', help='Print version and die')
    parser.add_argument('-O', '--color', action='store_true', help='Print color')
    parser.add_argument('-S', '--strip', action='store_false', help='Dont strip blank end or bottom')
    parser.add_argument('-T', '--timestamp', action='store_true', help='add timestamp of access time')
    parser.add_argument('-Z', '--sanitize', action='store_true', help='sanitize name from weird chars')
    parser.add_argument('-Y', '--yes', action='store_false', help='Confirm before rename [y/n]')
    parser.add_argument('-v', '--verbose', action='store_true', help='verbose output')

    # get args
    args = parser.parse_args()

    if args.version:
        print("Version ", Version)
        sys.exit(0)

    if not any([args.start, args.skip, args.space, args.contains, args.replace, args.force, args.pattern, args.lower, args.upper, args.camel, args.number, args.extlower, args.extension, args.sanitize, args.swap, args.verbose]):
        print("Version ", Version)
        parser.print_help()
        print("Sorry but I have nothing to do, did you try with some flags?\n\n")
        sys.exit(0)

    if args.color:
        color()

    # If it is piped to other program (i.e. rename.py... | less) than don't color print!
    if not os.isatty(1):
        nocolor()

    os.chdir(args.root)
    # Where to start, what to get
    if args.recursive:
        for top, subdirs, files in os.walk(a.root):
            for d in subdirs:
                newdir = os.path.join(top, d)
                os.chdir(newdir)
                bulk_rename(a)
    else:
        bulk_rename(args)


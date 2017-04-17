#!/usr/bin/env python3
# ernitron (c) 2017
# Mit License


import os
import sys
import re

# To print colored text on term
RED   = '\033[1;31m'
BLUE  = '\033[1;34m'
CYAN  = '\033[1;36m'
GREEN = '\033[0;32m'
RESET = '\033[0;0m'
BOLD  = '\033[;1m'
REV   = '\033[;7m'

def camel_case(fname):
    '''Convert to camel case: returns newname'''
    oldname = fname.replace('_', ' ')
    modified_name = re.findall('[\w]+', oldname.lower())
    return ''.join([word.title() for word in modified_name])

def replace_space(fname, fill_char='_'):
    '''Replace spaces with fill_char: fill_char: default to '_' :returns newname '''
    return fname.replace(' ', fill_char)

def replace_content(fname, contains=None, replace=None):
    if contains and contains in path:
        if replace is not None:
            return fname.replace(contains, replace)
    return fname

def lower_case(fname):
    '''Lower filename :returns newname '''
    return fname.lower()

def upper_case(fname):
    '''Upper filename :returns newname '''
    return fname.upper()

def skip_name(fname, start=None, skip=None):
    '''Skip in filename: returns: newname '''
    startlen = 0
    if start and fname.startswith(start):
        startlen += len(start)
    if skip and skip.isdigit():
        startlen += int(skip)
    # Initialize newname
    return fname[startlen:]

def add_number(fname, counter):
     return '%02d-%s' % (counter, fname)

def add_endnum(fname, counter):
     return '%s-%02d' % (fname, counter)

def substitute(fname, pattern, sub):
    try:
        spb = pattern.split('/')
        return re.sub(spb[1], spb[2], fname)
    except:
        pass

    if not sub: sub = ''
    return re.sub(pattern, sub, fname)

def renaming(start=None, skip=None, contains=None, replace=None, number=False, endnum=False, suffix=None, force=False, verbose=False,  tolow=False, toupper=False, camel=False, pattern=None, sub=None):
    counter = 1
    endcounter = 1
    for filename in os.listdir('.'):
        newname, extension = os.path.splitext(filename)
        extension = extension.lower()

        if suffix and not suffix in extension:
            continue
        if contains and not contains in path:
            continue
        if verbose:
            print(CYAN, filename, RESET)

        if start or skip:
            newname = skip_name(newname, start, skip)
        if contains and replace:
            newname = replace_content(newname, contains, replace)
        if camel:
            newname = camel_case(newname)
        if toupper:
            newname = upper_case(newname)
        if tolow:
        if pattern:
            newname = substitute(newname, pattern, sub)
        if number:
            newname = add_number(newname, counter)
            counter += 1
        if endnum:
            newname = add_endnum(newname, counter)
            endcounter += 1

        newname = newname + extension

        do_rename(filename, newname, force)

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

    parser.add_argument('--root', default='.')
    parser.add_argument('-s', '--start', help='replace start of filename', default=None)
    parser.add_argument('-c', '--contains', help='check if contains pattern', default=None)
    parser.add_argument('-r', '--replace', help='replace pattern of contains', default=None)
    parser.add_argument('-x', '--suffix', help='it must have suffix like .mp3', default=None)
    parser.add_argument('-k', '--skip', help='skip this number of char from file', default=None)
    parser.add_argument('-p', '--pattern', help='pattern', default=None)
    parser.add_argument('-b', '--sub', help='substitution', default=None)
    # Bool
    parser.add_argument('-n', '--number', action='store_true', help='add a 2 digit sequence start of filename', default=False)
    parser.add_argument('-e', '--endnum', action='store_true', help='add a 2 digit sequence end of filename', default=False)
    parser.add_argument('-f', '--force', action='store_true', help='force to rename otherwise it just print', default=False)
    parser.add_argument('-R', '--recursive', action='store_true', help='Recursive', default=False)
    parser.add_argument('-u', '--upper', action='store_true', help='To upper', default=False)
    parser.add_argument('-l', '--lower', action='store_true', help='To lower', default=False)
    parser.add_argument('-C', '--camel', action='store_true', help='CamelCase', default=False)
    parser.add_argument('-v', '--verbose', action='store_true', help='verbose output', default=False)

    # get args
    args = parser.parse_args()
    if not any([args.start, args.contains, args.replace, args.skip, args.force, args.pattern, args.sub, args.lower, args.upper, args.camel, args.verbose]):
        parser.print_help()
        sys.exit(0)

    # Where to start, what to get
    root = os.path.abspath(args.root)
    current_dir = os.path.dirname('./')
    os.chdir(current_dir)
    renaming(args.start, args.skip, args.contains, args.replace, args.number, args.endnum, args.suffix, args.force, args.verbose, args.lower, args.upper, args.camel, args.pattern, args.sub)

    if args.recursive:
      for top, subdirs, files in os.walk(root):
        for d in subdirs:
            newdir = os.path.join(top, d)
            os.chdir(newdir)
            renaming(args.start, args.skip, args.contains, args.replace, args.number, args.endnum, args.suffix, args.force, args.verbose, args.lower, args.upper, args.camel, args.pattern, args.sub)

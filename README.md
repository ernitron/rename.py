# rename.py

This is a rename.py application

# Requirements

Software: based on python 3

# USAGE

    usage: rename.py [-h] [--root ROOT] [-s START] [-c CONTAINS] [-r REPLACE] [-x SUFFIX] [-k SKIP] [-p PATTERN] [-b SUB] [-n]
                 [-e] [-f] [-R] [-u] [-l] [-C] [-v]

rename files

    optional arguments:

  -h, --help            show this help message and exit
  --root ROOT
  -s START, --start START
                        replace start of filename
  -c CONTAINS, --contains CONTAINS
                        check if contains pattern
  -r REPLACE, --replace REPLACE
                        replace pattern of contains
  -x SUFFIX, --suffix SUFFIX
                        it must have suffix like .mp3
  -k SKIP, --skip SKIP  skip this number of char from file
  -p PATTERN, --pattern PATTERN
                        pattern
  -b SUB, --sub SUB     substitution
  -n, --number          add a 2 digit sequence start of filename
  -e, --endnum          add a 2 digit sequence end of filename
  -f, --force           force to rename otherwise it just print
  -R, --recursive       Recursive
  -u, --upper           To upper
  -l, --lower           To lower
  -C, --camel           CamelCase
  -v, --verbose         verbose output

Examples:

    rename.py --start start_of_file --skip 5 --contains This --replace That --number --suffix .mp3 --force
    would rename a file like: start_of_file1234_Take_This.mp3
                     into: 01-Take_That.mp3

    rename.py -s start_of_file -p '/This/That/' -k 5 -n -x mp3 -f
    rename.py -s start_of_file -p This -b That -k 5 -n -x mp3 -f
    would do the same
 
## Installation


## Configuration

## Development

There is plenty of space for development




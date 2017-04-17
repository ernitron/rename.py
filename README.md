# rename.py
Yet another rename.py (should I really call it yaren.py?)
My Own Rename (bulk file rename python command line application) ala Perl rename.pl 

# Requirements
Software: works with python 3 (but I guess with 2.7 is ok)

# USAGE
    usage: rename.py [-h] [--root ROOT] [-b SUB] [-c CONTAINS] [-k SKIP]
                 [-m MATCH] [-p PATTERN] [-r REPLACE] [-s START] [-x SUFFIX]
                 [-a] [-e] [-f] [-n] [-u] [-l] [-R] [-C] [-v] [-V] [-L]

rename files!

    optional arguments:
    -h, --help            show this help message and exit
    --root ROOT   
    -c CONTAINS, --contains CONTAINS check if contains pattern; works with -r
    -r REPLACE, --replace REPLACE replace string; works with -c or -p)
    -k SKIP, --skip SKIP  skip this number of char from file
    -m MATCH, --match MATCH apply only to file that match pattern
    -p PATTERN, --pattern PATTERN pattern WITH REGEX 
    -s START, --start START replace start of filename
    -x SUFFIX, --suffix SUFFIX apply only file with suffix like .mp3
    -a, --space           no space or replace space
    -e, --endnum          add a 2 digit sequence end of filename
    -f, --force           force to rename otherwise it just print
    -n, --number          add a 2 digit sequence start of filename
    -u, --upper           To upper
    -l, --lower           To lower
    -R, --recursive       Recursive
    -C, --camel           CamelCase
    -v, --verbose         verbose output
    -V, --version         print version
    -L, --nocolor         print version

Examples:

    rename.py --start start_of_file --skip 5 --contains This --replace That --number --suffix .mp3 --force
    would rename a file like: start_of_file1234_Take_This.mp3
                     into: 01-Take_That.mp3

    rename.py -s start_of_file -p '/This/That/' -k 5 -n -x mp3 -f
    rename.py -s start_of_file -p This -b That -k 5 -n -x mp3 -f
    would do the same

    
# Examples

    rename.py --start start_of_file --skip 5 --contains This --replace That --number --suffix .mp3 --force
    would rename a file like: start_of_file1234_Take_This.mp3
                     into: 01-Take_That.mp3

    rename.py -s start_of_file -p '/This/That/' -k 5 -n -x mp3 -f
    rename.py -s start_of_file -p This -b That -k 5 -n -x mp3 -f
    would do the same
The Pattern and Sub can be REGULAR Expression as they will be feeded into python re.sub(pattern, sub, string)
Besides, pattern can be in the form of:

    's/ALPHA.*/Beta/' 
that will result in: 

    pattern='ALPHA.*' 
    sub='Beta'
and will work.

## Installation

Easy as make install
(will simply copy the file rename.py in /usr/local/bin)


## Configuration
Do we need one?

## Development
There is plenty of space for development

## License MIT
What other decent licenses exists?

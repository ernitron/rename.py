# rename.py
Yet another rename.py (should I really call it yaren.py?)
My Own Rename (bulk file rename python command line application) ala Perl rename.pl 

# Requirements
Software: works with python 3 (but I guess with 2.7 is ok)

# USAGE

    usage: rename.py [-h] [--root ROOT] [-c CONTAINS] [-p PATTERN] [-r REPLACE]
                 [-k SKIP] [-m MATCH] [-x SUFFIX] [-f] [-A] [-C] [-E] [-N]
                 [-D] [-F] [-U] [-L] [-R] [-V] [-O] [-v]

rename files

    optional arguments:
      -h, --help            show this help message and exit
      --root ROOT
      -c CONTAINS, --contains CONTAINS
                            check for string in filename; works with -r
      -p PATTERN, --pattern PATTERN
                            pattern with regex
      -r REPLACE, --replace REPLACE
                            replace for match string; works with -c and -p
      -s START, --skip START  start the string from file
      -k SKIP, --skip SKIP  skip this number of char from file
      -m MATCH, --match MATCH
                            apply only to file that match pattern
      -x SUFFIX, --suffix SUFFIX
                            apply only file with suffix like .mp3
      -f, --force           force to rename otherwise it just print
      -A, --space           replace space with _
      -C, --camel           CamelCase
      -E, --endnum          add a 2 digit sequence end of filename
      -N, --number          add a 2 digit sequence start of filename
      -D, --directory       apply only to directory
      -F, --regular         apply only to regular files
      -U, --upper           To upper
      -L, --lower           To lower
      -R, --recursive       Recursive
      -V, --version         print version
      -O, --nocolor         print version
      -v, --verbose         verbose output

Examples:

    rename.py --start start_of_file --skip 5 --contains This --replace That --number --suffix .mp3 --force
    would rename a file like: start_of_file1234_Take_This.mp3
                     into: 01-Take_That.mp3

    rename.py -s start_of_file -p '/This/That/' -k 5 -n -x mp3 -f
    rename.py -s start_of_file -p This -r That -k 5 -n -x mp3 -f
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

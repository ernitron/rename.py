# rename.py
Yet another rename.py (should I really call it yaren.py?)
My Own Rename (bulk file rename python command line application) ala Perl rename.pl 

# Requirements
Software: works with python 3 (but I guess with 2.7 is ok)

# USAGE
    usage: rename.py [-h] [--root ROOT] [-a [SPACE]] [-c CONTAINS] [-p PATTERN]
                     [-r REPLACE] [-k SKIP] [-s START] [-n [NUMBER]] [-m MATCH]
                     [-x SUFFIX] [-f] [-B] [-C] [-D] [-F] [-L] [-E] [-U] [-R] [-V]
                     [-O] [-S] [-T] [-Y] [-v]

rename files

    optional arguments:
      -h, --help            show this help message and exit
      --root ROOT           this will be the root directory
      -a [SPACE], --space [SPACE]
                            Replace space with _
      -c CONTAINS, --contains CONTAINS
                            check for string in filename; works with -r
      -p PATTERN, --pattern PATTERN
                            pattern with regex
      -r REPLACE, --replace REPLACE
                            replace string; works with -c and -p
      -k SKIP, --skip SKIP  skip this number of char from filename
      -s START, --start START
                            delete string from beginning of filename
      -n [NUMBER], --number [NUMBER]
                            Add a 2 digit sequence start of filename
      -m MATCH, --match MATCH
                            apply only to file that match pattern
      -x SUFFIX, --suffix SUFFIX
                            apply only to file with suffix like .mp3
      -f, --force           Force to rename (do it!)
      -B, --bottom          put sequence at end
      -C, --camel           Transform filename in CamelCase
      -D, --directory       Apply only to directory
      -F, --regular         Apply only to regular files
      -L, --lower           Transform filename into lower case
      -E, --extlower        Transform extension into lower case
      -U, --upper           Transform filename into upper case
      -R, --recursive       Recursive into subdirs
      -V, --version         Print version and die
      -O, --color           Print color
      -S, --strip           Dont strip blank end or bottom
      -T, --timestamp       add timestamp of access time
      -Y, --yes             Confirm before rename [y/n]
      -v, --verbose         verbose output

            Examples:
            rename.py --skip start_of_file --skip 5 --contains This --replace That --number --suffix .mp3 --force
            would rename a file like: start_of_file1234_Take_This.mp3
                         into: 01-Take_That.mp3

            rename.py -k start_of_file -p '/This/That/' -k 5 -n -x mp3 -f
            rename.py -k start_of_file -p This -r That -k 5 -n -x mp3 -f
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


## Development
There is plenty of space for development

## License MIT
What other decent licenses exist?

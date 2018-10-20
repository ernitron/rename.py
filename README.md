# rename.py
Yet another rename.py (should I really call it yaren.py?)
My Own Rename (bulk file rename python command line application) ala Perl rename.pl 

# Requirements
Software: works with python 3 

# USAGE

    usage: yaren.py [-h] [-a STRING] [-b [BLANK]] [-c CONTAINS] [-d DELETE]
                    [-e EXPRESSION] [-r REPLACE] [-s START] [-z ZTRIP] [-k SKIP]
                    [-n [NUMBER]] [-w [SWAP]] [-ext EXTENSION] [-exl]
                    [--root ROOT] [-m MATCH] [-x SUFFIX] [-D] [-G] [-R] [-Y] [-F]
                    [-_] [-B] [-C] [-L] [-U] [-T] [-V] [-O] [-S] [-P] [-Z]
                    [-H [HASH]] [-v] [--remove]
                    [files [files ...]]

    rename files

    positional arguments:
      files

    optional arguments:
      -h, --help            show this help message and exit
      -a STRING, --string STRING
                            add string
      -b [BLANK], --blank [BLANK]
                            Replace blank with _
      -c CONTAINS, --contains CONTAINS
                            check for string in filename; works with -r
      -d DELETE, --delete DELETE
                            delete string in filename
      -e EXPRESSION, --expression EXPRESSION
                            pattern with regex
      -r REPLACE, --replace REPLACE
                            replace string; works with -c and -p
      -s START, --start START
                            delete string from beginning of filename
      -z ZTRIP, --ztrip ZTRIP
                            delete n chars from end of filename
      -k SKIP, --skip SKIP  skip n char from start of filename
      -n [NUMBER], --number [NUMBER]
                            Add a 2 digit sequence
      -w [SWAP], --swap [SWAP]
                            swap names Alfa Beta->Beta Alfa
      -ext EXTENSION, --extension EXTENSION
                            change extension example to .mp3
      -exl, --extlower      Transform extension into lower case
      --root ROOT           this will be the root directory
      -m MATCH, --match MATCH
                            apply only to file that match pattern
      -x SUFFIX, --suffix SUFFIX
                            apply only to file with suffix like .mp3
      -D, --directory       Apply only to directory
      -G, --regular         Apply only to regular files
      -R, --recursive       Recursive into subdirs
      -Y, --yes             Confirm before rename [y/n]
      -F, --force           Force to rename (do it!)
      -_, --under           Remove underscores and minuses
      -B, --bottom          Put number sequence at end
      -C, --camel           Transform filename in CamelCase
      -L, --lower           Transform filename into lower case
      -U, --upper           Transform filename into upper case
      -T, --title           Transform into Title case
      -V, --version         Print version and die
      -O, --color           Print messages in color
      -S, --strip           Strip blank|tab at end or bottom
      -P, --timestamp       Add timestamp of access time
      -Z, --sanitize        Sanitize name from weird chars
      -H [HASH], --hash [HASH]
                            filename is hash
      -v, --verbose         verbose output
      --remove              remove file if match

        Examples:
        $ rename.py --skip start_of_file --skip 5 --contains This --replace That --number --suffix .mp3 --force
        would rename a file like: start_of_file1234_Take_This.mp3
                     into: 01-Take_That.mp3

        $ rename.py -s start_of_file -k 5 -e '/This/That/' -n -x mp3 -F
        would do the same
     
## Installation
Easy as make install
(will simply copy the file rename.py in /usr/local/bin)

## Development
There is plenty of space for development

## License MIT
What other decent licenses exist?

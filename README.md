# rename.py
Yet another rename.py (should I really call it yaren.py?)
My Own Rename (bulk file rename python command line application) ala Perl rename.pl 

# Requirements
Software: works with python 3 (but I guess with 2.7 is ok)

# USAGE
    usage: rename.py [-h] [-a [SPACE]] [-c CONTAINS] [-e EXTENSION] [-p PATTERN]
                     [-r REPLACE] [-s START] [-k SKIP] [-z ZTRIP] [-n [NUMBER]]
                     [-w [SWAP]] [--root ROOT] [-m MATCH] [-x SUFFIX]
                     [-f [FILES [FILES ...]]] [-F] [-_] [-B] [-C] [-D] [-G] [-L]
                     [-E] [-U] [-T] [-R] [-V] [-O] [-S] [-P] [-Z] [-Y] [-H] [-v]

    rename files

    optional arguments:
      -h, --help            show this help message and exit
      -a TEXT, --add TEXT
                            add text to filename
      -b [SPACE], --blank [SPACE]
                            Replace space with _
      -c CONTAINS, --contains CONTAINS
                            check for string in filename; works with -r
      -e EXTENSION, --extension EXTENSION
                            change extension example to .mp3
      -p PATTERN, --pattern PATTERN
                            pattern with regex
      -r REPLACE, --replace REPLACE
                            replace string; works with -c and -p
      -s START, --start START
                            delete string from beginning of filename
      -k SKIP, --skip SKIP  skip n char from start of filename
      -z ZTRIP, --ztrip ZTRIP
                            delete n chars from end of filename
      -n [NUMBER], --number [NUMBER]
                            Add a 2 digit sequence start of filename
      -w [SWAP], --swap [SWAP]
                            swap names Alfa Beta->Beta Alfa
      --root ROOT           this will be the root directory
      -m MATCH, --match MATCH
                            apply only to file that match pattern
      -x SUFFIX, --suffix SUFFIX
                            apply only to file with suffix like .mp3
      -f [FILES [FILES ...]], --files [FILES [FILES ...]]
                            apply to list of files
      -F, --force           Force to rename (do it!)
      -_, --under           Force to rename (do it!)
      -B, --bottom          put sequence at end
      -C, --camel           Transform filename in CamelCase
      -D, --directory       Apply only to directory
      -G, --regular         Apply only to regular files
      -L, --lower           Transform filename into lower case
      -E, --extlower        Transform extension into lower case
      -U, --upper           Transform filename into upper case
      -T, --title           Transform into Title case
      -R, --recursive       Recursive into subdirs
      -V, --version         Print version and die
      -O, --color           Print color
      -S, --strip           Strip blank|tab at end or bottom
      -P, --timestamp       add timestamp of access time
      -Z, --sanitize        sanitize name from weird chars
      -Y, --yes             Confirm before rename [y/n]
      -H, --hash            hash 256
      -v, --verbose         verbose output

	Examples:
	rename.py --skip start_of_file --skip 5 --contains This --replace That --number --suffix .mp3 --force
	would rename a file like: start_of_file1234_Take_This.mp3
                     into: 01-Take_That.mp3

	rename.py -s start_of_file -k 5 -p '/This/That/' -n -x mp3 -F
	rename.py -k start_of_file1234_ -p This -r That -n -x mp3 -F
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

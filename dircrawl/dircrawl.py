#!/usr/bin/env python3

import os, re, sys
from termcolor import colored, cprint

def main():
    if len(sys.argv) < 2:
        print('''
    Usage:
        This program will search for instances of the word "password" within a file or directory.

        Options:
        dir  -   Search the files in the current Directory
        -R   -   Search the files in this directory and all directories in it
        -f   -   Search a specific file

        Examples:
        dir
        -R
        -f web.config
        ''')
    elif  sys.argv[1] == "dir":
        try:
            lookForPasswords = re.compile(r'.*password.*', re.I)
            passwordcolor = re.compile(r'password', re.I)
            for filename in os.listdir():
                pathOfFile = '.' + '/' + filename
                try:
                    files = open(pathOfFile)
                    text = files.read()
                    foundText = lookForPasswords.search(text)
                    files.close()
                    if foundText != None:
                        matchedText = passwordcolor.search(foundText.group())
                        coloredText = colored (matchedText.group() , 'red')
                        highlightedText = passwordcolor.sub(coloredText, foundText.group())
                        cprint(pathOfFile, 'green')
                        cprint(highlightedText)
                except (UnicodeDecodeError, FileNotFoundError, IsADirectoryError) as exception:
                    continue
        except KeyboardInterrupt as exception:
            print("\nUser interrupt detected. Stopping.")
    else:
        try:
            if sys.argv[1] == "-R":
                lookForPasswords = re.compile(r'.*password.*', re.I)
                passwordcolor = re.compile(r'password', re.I)
                for folders, subforlders, filenames in os.walk('.'):
                    for filename in filenames:
                        pathOfFile = folders + '/' + filename
                        try:
                            files = open(pathOfFile)
                            text = files.read()
                            foundText = lookForPasswords.search(text)
                            files.close()
                            if foundText != None:
                                matchedText = passwordcolor.search(foundText.group())
                                coloredText = colored (matchedText.group() , 'red')
                                highlightedText = passwordcolor.sub(coloredText, foundText.group())
                                cprint(pathOfFile, 'green')
                                cprint(highlightedText)
                        except (UnicodeDecodeError, FileNotFoundError) as exception:
                            continue
        except KeyboardInterrupt as exception:
            print("\nUser interrupt detected. Stopping.")

if __name__=='__main__':
    main()
    sys.exit()

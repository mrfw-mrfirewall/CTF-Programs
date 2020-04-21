# dircrawl.py
A python script for crawling files and directories for interesting text.
The script is a work in progress. The only dependency at this time is "termcolor" which can be installed with `pip3 install termcolor`. I had not realized it was not a default module and may rewrite it to only include native modules.

The `-f` option is not yet implemented. 

I plan to add other options and features such as the following:
- Adding more terms to search for: e.g. "admin", "hash", "aes256"
- Allowing the user to specify custom words to search for.

            Usage:
                This program will search for instances of the word "password" within a file or directory.
                
                Options:
                dir  -   Search the files in the current Directory
                -R   -   Search the files in this directory and all directories in it
                -f   -   Search a specific file
                
                Examples:
                dir
                -R
                -f web.configs

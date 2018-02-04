#!usr/bin/env python
import re, os, shutil

#create regex to find american name
amerNameRegex = re.compile(('''
    (\w*)                    #name of file before date
    ([0][1-9]|1[012])        #month
    ([-/])?                  #separator (optional)
    (0[1-9]|[12][0-9]|3[01]) #day
    ([-/])?                  #separator (optional)
    ([12][90][0-9][0-9])     #year
    (\w*)                    #name of file after date (with ext)
    (\..+)?                  #extension
    '''), re.VERBOSE)

#cd to the correct directory
os.chdir('/home/justin/Python-Workspace/AutomateTheBoringStuff/Chapter 9/DatedFiles')
#find all instances of files with american names in the directory
for file in os.listdir():
    matchf =  amerNameRegex.match(file)
    if matchf:
        ls = list(matchf.groups())
        tmp = ls[1]
        ls[1] = ls[3]
        ls[3] = tmp
        ls = [x for x in ls if x != None]
        newname = "".join(ls)
#flip the date and month spot on each found file with shutil.move
        shutil.move(file, newname)


#print message of completion
print('end of program')

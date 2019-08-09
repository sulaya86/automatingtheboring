"""
Find and Move or Copy Files listed in a txt document from a given source to a target folder
and print on the screen how many files where transferred
Useful when  you work with UNC paths and files are in different server locations and local computer.
"""
import os
from shutil import copy2, move
TXTFILES = []

#The path where your txt file is
FILE_PATH = r'D:\\your\\ownfolder\\'

SOURCE_PATH = r'\\servername\\canbeUNC\\'
DESTINY_PATH = r'D:\\another\\folder\\inlocal\\'

#If the files are not found in the source they will be listed
NOT_FOUND_FILES = FILE_PATH + 'files_not_found.txt'

#To keep a record of the files that were found
FOUND_FILES = FILE_PATH + 'files_found.txt'

with open(FILE_PATH + 'files.txt') as f:
    COUNT = 0 
    for line in f:
        line = line.rstrip('\n')

        exists = os.path.isfile(SOURCE_PATH + line)
        if exists:
            print(line)
            copy2(os.path.abspath(SOURCE_PATH + line), os.path.abspath(DESTINY_PATH + line))
            #move(os.path.abspath(SOURCE_PATH + line), os.path.abspath(DESTINY_PATH + line))
            with open(FOUND_FILES, 'a') as file_out:
                file_out.write(f'\n{line}')
            COUNT += 1
            if 'str' in line:
                break
        else:
            print("not exist: " + SOURCE_PATH + line)
            with open(NOT_FOUND_FILES, 'a') as file_out:
                file_out.write(f'\n{line}')


print(COUNT)

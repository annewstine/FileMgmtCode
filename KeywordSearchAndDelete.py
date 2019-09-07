#Searches for files containing keyword and deletes them. Prints number of files deleted. 

import fnmatch
import os

mypath = 'C:\\Users\\...\\targetfolder'

deleted = 0
for file in os.listdir(mypath):
    if fnmatch.fnmatch(file, '*SEARCH_TEXT*'):
        print(file + ' deleting...')
        deleted += 1
        os.remove(os.path.join(mypath, file))
        print(str(deleted) + ' file(s) deleted')

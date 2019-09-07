import fnmatch
import os

mypath = 'C:\\Users\\AStine\\PycharmProjects\\pdf2jpg\\testpdfs'

deleted = 0
for file in os.listdir(mypath):
    if fnmatch.fnmatch(file, '*Copy*'):
        print(file + ' deleting...')
        deleted += 1
        os.remove(os.path.join(mypath, file))
        print(str(deleted) + ' file(s) deleted')
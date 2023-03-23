#!/usr/bin/python3
import os

DIR = '/dir1'
if __name__ == "__main__" :
    newDir = os.getcwd()+DIR
    if os.path.isdir(newDir) is False:
        print('{} not exists and should be created'.format(newDir))
        os.mkdir(newDir)
    else:
        print('{} already exists'.format(newDir))

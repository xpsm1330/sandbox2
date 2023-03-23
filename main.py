#!/usr/bin/python3
import os

def create_file(location, fileName, amount):
    for i in range(amount):
        with open(location+'/'+fileName+str(i), 'w') as fp:
            pass

    listDir = os.listdir(location)
    print('{} contains {}'.format(location, listDir))

DIR = '/dir1'
if __name__ == "__main__" :
    newDir = os.getcwd()+DIR
    if os.path.isdir(newDir) is False:
        print('{} not exists and should be created'.format(newDir))
        os.mkdir(newDir)
    else:
        print('{} already exists'.format(newDir))

    create_file(newDir, 'test', 5)

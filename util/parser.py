import os

def parser():
    f = open('cmd.txt', 'r')
    path = '/home/anhong-eun/Desktop/bbbb'
    os.chdir(path)
    lines = f.readlines()
    for cmd in lines:
        os.system(cmd)
import os

f = open('cmd.txt', 'r')
lines = f.readlines()
for cmd in lines:
    os.system(cmd)
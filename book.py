#!/bin/python
import sys, os, os.path
from focus import focus
foc='focus>'
#name_file=input('name>')
#name_file=sys.argv[1]
if sys.argv[1]=='-v' or sys.argv[1]=='--version':
    print('version.1.1')
    sys.exit()
if sys.argv[1]=='-c':
    os.system('python3 calc')
    sys.exit()
if sys.argv[1]!='-o'and sys.argv[1]!='-h'and sys.argv[1]!='-help':
    name_file=sys.argv[1]
elif sys.argv[1]=='-h' or sys.argv[1]=='--help':
    os.system('cat info.txt')
    sys.exit()
elif sys.argv[1]=='-o':
    os.system(f'cat {sys.argv[2]}')
    sys.exit()
if os.path.isfile(name_file):
    with open(name_file,'r') as file:
            print(file.read(),end='')
while True:
    fog=input()
    if fog=='exit':
        break
    elif foc in fog:
        with open('test/' + name_file,'a') as file:
            file.write(focus(fog))
    else:
        with open('test/' + name_file,'a') as file:
            file.write(fog + '\n')



import sys
import os
import shutil

if len(sys.argv)<3:
    print("Zla liczba argumentow")
    exit()

if not os.path.isdir(sys.argv[1]):
    print("'{}' is not directory".format(sys.argv[1]))
    exit()
    
if not os.path.isfile(sys.argv[2]):
    print("'{}' is not file".format(sys.argv[2]))
    exit()


f = open(sys.argv[2])
for line in f.readlines():
    #os.mkdir(os.path.join(sys.argv[1],line[:-1]))
    open(os.path.join(sys.argv[1],line[:-1]),'a+').close()

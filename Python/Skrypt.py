#!/usr/bin/env python3
##2
import sys
import os

if len(sys.argv)<2:
    print("Zla liczba argumentow")
    exit()

if not os.path.isdir(sys.argv[1]):
    print("'{}' is not directory".format(sys.argv[1]))
    exit()

f = open(sys.argv[2])
files_list = set([line[:-1] for line in f.readlines()])
files_in_dir = set([file for file in os.listdir(sys.argv[1])])

a = list(files_in_dir)
b = list(files_list)

for f in a:
    for x in b:
      if x == f:
       os.remove((os.getcwd()+"/"+ sys.argv[1]+"/"+x))




for file in os.listdir(sys.argv[1]):
    path = os.path.join(sys.argv[1],file)
    if os.path.lexists(path) == bool(1): 
       os.remove(path)




for root, dirs, files in os.walk(sys.argv[1]):
    for file in files:
      tmpfile = os.path.join(root, file)
      if os.access(tmpfile, os.R_OK):
         print(tmpfile)

    for dir in dirs:
        tmpDir = os.path.join(root, dir)
        dirCount = 0
        for fileInDir in os.listdir(tmpDir):
            tmpFileInDir = os.path.join(tmpDir, fileInDir)
            if os.path.isdir(tmpFileInDir):
               dirCount += 1
               if dirCount >= 2:
                  print(tmpDir + " posiada conajmniej 2 katalogi")
                  break


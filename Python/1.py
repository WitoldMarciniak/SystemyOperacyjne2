#!/usr/bin/env python3
##1
import sys
import os


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
files_list = set([line[:-1] for line in f.readlines()])
files_in_dir = set([file for file in os.listdir(sys.argv[1])])

a = list(files_in_dir)
b = list(files_list)

for f in a:
    for x in b:
      if x == f:
       os.remove((os.getcwd()+"/"+ sys.argv[1]+"/"+x))


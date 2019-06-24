#!/usr/bin/env python3
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

print('pliki usuniete:')
for f in files_list.intersection(files_in_dir):
 ','.join(str(s) for s in files_list)

      print(s)

  


print('pliki których brakuje na liście:')
for f in files_in_dir.difference(files_list):
    print(f)

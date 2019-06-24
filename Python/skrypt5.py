#!/usr/bin/env python3

import sys
import os

if len(sys.argv)<2:
    print("Zla liczba argumentow")
    exit()

if not os.path.isdir(sys.argv[1]):
    print("'{}' is not directory".format(sys.argv[1]))
    exit()

for file in os.listdir(sys.argv[1]):
    path = os.path.join(sys.argv[1],file)
    if os.path.isfile(path):
       if os.access(path, os.W_OK):
         (filepath, filename) = os.path.split(path)
         (filename, extension) = os.path.split(filename)
         f = open(path, "r")
	  
         print(file +" "+ f.read())

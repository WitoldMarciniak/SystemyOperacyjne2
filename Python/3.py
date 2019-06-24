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


  

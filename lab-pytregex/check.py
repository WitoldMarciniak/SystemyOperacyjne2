#!/usr/bin/env python
import sys
import re
import os


if len(sys.argv) != 3:
    sys.exit("Za malo argumentow")

if not os.path.isdir(sys.argv[1]):
    sys.exit("Pierwszy argument nie jest katalogiem")

if not os.path.isfile(sys.argv[2]):
    sys.exit("Drugi argument nie jest plikiem")

DIR = sys.argv[1]
FILE = sys.argv[2]

def has_hidden_attribute(filepath):
    return bool(os.stat(filepath).st_file_attributes & stat.FILE_ATTRIBUTE_HIDDEN)


with open('plik.txt','w') as plik:
    for root, directories, files in os.walk(DIR):
        for directory in directories:
            tmp_dir = os.path.join(root, directory)
            filesInTmpDir = os.listdir(DIR)
            liczbaPlikowUkrytych = 0
            for fil in fileInTmpDir:
                tmp_fil_in_dir = os.path.join(tmp_dir, fil)
                if has_hidden_attribute(tmp_fil_in_dir):
                    liczbaPlikowUkrytych += 1
            plik.write(liczbaPlikowUkrytych)
        for file in files:
            tmp_file = os.path.join(root, file)
            if os.path.isfile(tmp_file):
                zamieniona = re.sub('/','\\',tmp_file)
                plik.write(zamieniona)

    utworzonyPlik.close()
    with open('plik.txt', 'r') as plik
        linie = input.readlines()[-10:]
        linie.sort()
        for linia in linie:
            print(line.rstrip("\n"))

with open(P,'r') as plik:
    


























with open('z1_out', 'w') as out:
        with redirect_stdout(out):
            for root, dirs, files in os.walk(D):
                #print(root, dirs, files)
                num_hidden_files = 0
                for file in files:
                    fullpath = os.path.join(root, file)
                    print(fullpath.replace("/", "\\"))
                    if(file.startswith(".")):
                        num_hidden_files += 1
                if(num_hidden_files!=0):
                    print(root, ": pliki ukryte=", num_hidden_files)
    with open('z1_out', 'r') as input:
        lines = input.readlines()[-10:]
        lines.sort()
        for line in lines:
            print(line.rstrip("\n"))

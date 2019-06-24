#!/usr/bin/env python3
import sys
import re
import os


if len(sys.argv) != 3:
    sys.exit("Za malo argumentow")

if not os.path.isdir(sys.argv[1]):
    sys.exit("Pierwszy argument nie jest katalogiem")

if not os.path.isfile(sys.argv[2]):
    sys.exit("Drugi argument nie jest plikiem")

plik = open('result.txt','w')

DIR = sys.argv[1]
FILE = sys.argv[2]
file_all = []
liczbaPlikowUkrytych = 0
for root, directories, files in os.walk(DIR):
    for directory in directories:
        tmp_dir = os.path.join(root, directory)
        filesInTmpDir = os.listdir(DIR)
        
        for fil in filesInTmpDir:
            tmp_fil_in_dir = os.path.join(tmp_dir, fil)
            if os.path.isfile(tmp_fil_in_dir):
                if tmp_fil_in_dir.startswith('.'):
                   liczbaPlikowUkrytych += 1
                   file_all.append(str(tmp_fil_in_dir))
                   plik.write(str(tmp_fil_in_dir))
    for x in files:
        tmp_file = os.path.join(root, x)
        if os.path.isfile(tmp_file):
              fullpath = os.path.join(root, x) 
              print(fullpath.replace("/", "\\"))
              plik.write(str(fullpath))
              file_all.append(str(fullpath))  
file_all.sort()
print(file_all[:10])
print(liczbaPlikowUkrytych)

plik.close()
p = re.compile('((([a-zA-Z])+):\/\/(([[a-zA-Z]+\.))*)([a-zA-Z])+')

with open(FILE) as f:
    content = f.read()
    x = re.search(p,content).group()
    print(str(x))

   
urls = re.findall(p,content)

##print(urls)
for item in urls:
   print(str(item[0]))

with open('xx', 'w') as f:
    f.write(str(urls))


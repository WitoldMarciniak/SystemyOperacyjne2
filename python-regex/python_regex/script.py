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
file_all = []

for root, directories, files in os.walk(DIR):
    for file in files:
        tmp_file = os.path.join(root, file)
        if os.path.isfile(tmp_file):
            size = os.path.getsize(tmp_file) / 100
            #file_all.append(size)
        if os.path.islink(tmp_file):
            link_to_path = os.readlink(tmp_file)
            file_all.append(link_to_path)

file_all.sort()

with open('sort.txt', 'w') as f:
    for item in file_all:
        f.write(str(item))

print(file_all[:10])


#drugie zadanie

p = re.compile('([0-9]{4})-(([0][1-9])|10|11|12)-(([0-2][0-9]|[^00])|31)')

with open(FILE) as f:
    content = f.read()

dates = re.findall(p, content)

for date in dates:
    oldDate = str(date[0]) + '-' + str(date[1]) + '-' + str(date[2])
    newDate = str(date[2]) + '/' + str(date[1]) + '/' + str(date[0][:2])
    content = re.sub(oldDate, newDate, content)


with open('xx', 'w') as f:
    f.write(content)

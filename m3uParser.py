__author__ = 'KingKoopa'
import os
import re
import csv
import urllib
import shutil
import glob, os
source = os.listdir("<-Path of Python Script->")
#Where it is going to save m3u mainfile
destination = "<-Path of Raw m3u File->"

#Clearing Old Files
directory='<-Path of Raw m3u File->'
os.chdir(directory)
files=glob.glob('*.m3u')
for filename in files:
    os.unlink(filename)

#Download New File
urllib.urlretrieve ("<-url of m3u list->", "<-filename->")


#Searches File For U.S. Streams
with open('<-Path of Raw m3u File->', 'r') as f:
    f2 = open('<-Path of edited File->', 'w')
    searchlines = f.readlines()
    for i, line in enumerate(searchlines):
        if "United States" in line:
            for l in searchlines[i:i+2]: print l,
            f2.write(line)
            f2.write(l)
f.close()
f2.close()

#Searches File For HD Sports without Cricket/Spanish
with open('<-Path of Raw m3u File->', 'r') as f:
    f2 = open('<-Path of edited File->', 'w')
    searchlines = f.readlines()
    for i, line in enumerate(searchlines):
        if "group-title=\"Sports\"" in line and (' '+'HD') in line:
            if  not 'Cricket' in line and not 'Deportes' in line and not 'Espanol' in line:
                for l in searchlines[i:i+2]: print l,
                f2.write(line)
                f2.write(l)
f.close()
f2.close()

#Searches File For Premium
with open('<-Path of Raw m3u File->', 'r') as f:
    f2 = open('<-Path of edited File->', 'w')
    searchlines = f.readlines()
    for i, line in enumerate(searchlines):
        if "group-title=\"Premium Movies\"" in line:
                for l in searchlines[i:i+2]: print l,
                f2.write(line)
                f2.write(l)
f.close()
f2.close()

#Searches File For LiveEvents
with open('<-Path of Raw m3u File->', 'r') as f:
    f2 = open('<-Path of edited File->', 'w')
    searchlines = f.readlines()
    for i, line in enumerate(searchlines):
        if "group-title=\"Live Events\"" in line:
                for l in searchlines[i:i+2]: print l,
                f2.write(line)
                f2.write(l)
f.close()
f2.close()

#Searches File For UK
with open('<-Path of Raw m3u File->', 'r') as f:
    f2 = open('<-Path of edited File->', 'w')
    searchlines = f.readlines()
    for i, line in enumerate(searchlines):
        if "BBC" in line and (' '+'HD') in line:
            if not 'America' in line:
                for l in searchlines[i:i+2]: print l,
                f2.write(line)
                f2.write(l)
f.close()
f2.close()

#Searches File For MatchCenter
with open('<-Path of Raw m3u File->', 'r') as f:
    f2 = open('<-Path of edited File->', 'w')
    searchlines = f.readlines()
    for i, line in enumerate(searchlines):
        if "MatchCenter" in line:
                for l in searchlines[i:i+2]: print l,
                f2.write(line)
                f2.write(l)
f.close()
f2.close()
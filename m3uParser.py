__author__ = 'KingKoopa'
import os
import re
import csv
import urllib
import shutil
import glob, os


#### Psource = os.listdir("<-Path of Python  - Script->")
#### Rawdest  = "<-Path of Raw - m3u File->"
#### Urlget = "<-url of m3u - list->"
#### Urlname = "<-file-name->"
#### Editdest = '<-Path of - edited File->'

Psource = os.listdir("<-Path of Python  - Script->")
Rawdest  = "<-Path of Raw - m3u File->"
Urlget = "<-url of m3u - list->"
Urlname = "<-Name of Raw m3u file->"
Editdest = '<-Path of - edited File->'
Editname = Urlname

#Where it is going to save m3u mainfile
destination = Rawdest

#Clearing Old Files
directory=Rawdest
os.chdir(directory)
files=glob.glob('*.m3u')
for filename in files:
    os.unlink(filename)

#Download New File
urllib.urlretrieve (Urlget, Urlname)


#Searches File For U.S. Streams
with open(Rawdest+Urlname, 'r') as f:
    f2 = open(Editdest+Urlname+"US"+".m3u", 'w')
    searchlines = f.readlines()
    for i, line in enumerate(searchlines):
        if "United States" in line:
            for l in searchlines[i:i+2]: print (l),
            f2.write(line)
            f2.write(l)
f.close()
f2.close()

#Searches File For Sports
with open(Rawdest+Urlname, 'r') as f:
    f2 = open(Editdest+Urlname+"Sports"+".m3u", 'w')
    searchlines = f.readlines()
    for i, line in enumerate(searchlines):
        if "group-title=\"Sports\"" in line and (' '+'HD') in line:
            if  not 'Cricket' in line and not 'Deportes' in line and not 'Espanol' in line:
                for l in searchlines[i:i+2]: print (l),
                f2.write(line)
                f2.write(l)
f.close()
f2.close()

#Searches File For Premium
with open(Rawdest+Urlname, 'r') as f:
    f2 = open(Editdest+Urlname+"Premium"+".m3u", 'w')
    searchlines = f.readlines()
    for i, line in enumerate(searchlines):
        if "group-title=\"Premium Movies\"" in line:
                for l in searchlines[i:i+2]: print (l),
                f2.write(line)
                f2.write(l)
f.close()
f2.close()

#Searches File For LiveEvents
with open(Rawdest+Urlname, 'r') as f:
    f2 = open(Editdest+Urlname+"LiveEvents"+".m3u", 'w')
    searchlines = f.readlines()
    for i, line in enumerate(searchlines):
        if "group-title=\"Live Events\"" in line:
                for l in searchlines[i:i+2]: print (l),
                f2.write(line)
                f2.write(l)
f.close()
f2.close()

#Searches File For UK
with open(Rawdest+Urlname, 'r') as f:
    f2 = open(Editdest+Urlname+"UK"+".m3u", 'w')
    searchlines = f.readlines()
    for i, line in enumerate(searchlines):
        if "BBC" in line and (' '+'HD') in line:
            if not 'America' in line:
                for l in searchlines[i:i+2]: print (l),
                f2.write(line)
                f2.write(l)
f.close()
f2.close()

#Searches File For MatchCenter
with open(Rawdest+Urlname, 'r') as f:
    f2 = open(Editdest+Urlname+"Matchcenter"+".m3u", 'w')
    searchlines = f.readlines()
    for i, line in enumerate(searchlines):
        if "MatchCenter" in line:
                for l in searchlines[i:i+2]: print (l),
                f2.write(line)
                f2.write(l)
f.close()
f2.close()
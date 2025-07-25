## ---------- DAY 11 Python -------- ##

## List of concepts to master Day 11 Python....../

"""
✅ Concepts to Include
1. open(), read(), write(), append()

2. with open(...) as f

3. seek(), tell()

4. os, os.path, shutil

"""

# Write a note
f = open("notes.txt", "w")
f.write("Today I learned file handling.")
f.close()

# Append another note
f = open("notes.txt", "a")
f.write("\nTomorrow I’ll learn about OS module.")
f.close()

# Read the diary
f = open("notes.txt", "r")
print(f.read())
f.close()

## ---->>> With Open of Context 

with open("notes.txt", "r") as f:
    content = f.read()
    print(content)  # Automatically closes the file after this block

## ----->>>> SEEK () & TELL () 

with open("notes.txt", "r") as f:
    print("Cursor at:", f.tell())       # ➝ 0
    print("First 10 chars:", f.read(10))
    print("Now cursor at:", f.tell())   # ➝ 10
    f.seek(0)                           # Back to beginning
    print("After seek:", f.read(10))    # ➝ same 10 chars
    print("Cursor at:", f.tell())       # ➝


## ------>>>> os, os.path, shutil — Working with Files & Folders

# os.module 
import os

print(os.getcwd())                # Current working directory
# os.mkdir("MyFolder")              # Make a new folder
os.rename("notes.txt", "log.txt") # Rename a file
os.remove("log.txt")              # Delete file

# os.path
import os
from os import path

print(path.exists("log.txt"))         # Check if file exists
print(path.isdir("MyFolder"))         # Is it a folder?
print(path.getsize("notes.txt"))      # File size in bytes

# shutil

import shutil

shutil.copy("notes.txt", "backup_notes.txt")       # Copy file
shutil.move("backup_notes.txt", "MyFolder/")       # Move file to folder
shutil.rmtree("MyFolder")                          # Delete folder and everything in it

import sys
import os
import glob

picTotal = 0


list_dir = os.listdir("input/")
for file in list_dir:
    if file.endswith(".jpg"): # eg: '.txt'
        picTotal += 1

print("PICTOTAL = ", picTotal)

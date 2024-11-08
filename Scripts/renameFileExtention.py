import os
import sys
folder = 'H:\AS400\OrdersJeff'
for filename in os.listdir(folder):
    infilename = os.path.join(folder, filename)
    if not os.path.isfile(infilename):
        continue
    oldbase = os.path.splitext(filename)
    newname = infilename.replace('.csv', '.txt')
    output = os.rename(infilename, newname)

import glob
import os

os.chdir = 'H:/AS400/OrdersJeff'
files = glob.glob(os.chdir + '\\*txt')

file_big = 'combined_txt.txt'

with open(file_big, 'wb') as fnew:
    for f in files:
        with open(f, 'rb') as fold:
            for line in fold:
                fnew.write(line)
                fnew.write("\n".encode(encoding='utf_8'))

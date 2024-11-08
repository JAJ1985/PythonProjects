from os.path import isfile, join
from os import listdir

mypath = "H:\\altaCart\\Projects\\sd_email"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print('f')

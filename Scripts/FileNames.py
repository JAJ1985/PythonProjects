import os

FOLDER_PATH = r'H:\\altaCart\\Projects\\sd_email'


def listDir(dir):
    fileNames = os.listdir(dir)
    for fileNames in fileNames:
        print('File Name: ' + fileNames)
        print('File Name:  ' + os.path.abspath(os.path.join(dir, fileNames)), sep='\n')


if __name__ == '__main__':
    listDir(FOLDER_PATH)

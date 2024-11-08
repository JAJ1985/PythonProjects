# Importing re module for creating a regex expression
import re
import csv
from pathlib2 import Path



file_path = input('Enter the file path:')

# replacements = {'AGENT' : 'A', 'CONSUMER' : 'C'}

'''
# This works - add to main
def extract_text_from_csv_file(file_path):
    with open(file_path, 'r') as file:
        csvreader = csv.reader(file)       
        for row in csvreader:           
            return row

def clean_data():
	with open(file_path, 'r') as file: 
		text = file.read() 		
	pattern = re.sub(r"[\([{})\]]", "", text)	
	with open('C:\Python\Data\outputCaseTestData1.txt', 'w') as my_file:
		my_file.write(pattern)

#This works
def remove_special_characters():
	with open(file_path, 'r') as f:
		text = f.read()
	pattern = re.sub(r"[\([{})\]]", ':' "", text)	
	with open('C:\Python\Data\outputCaseTestData1.txt', 'w') as my_file:
		my_file.write(pattern)



def replace_text(search_text, replace_text):
	file = Path(r'C:\Python\Data\outputCaseTestData1.txt')
	data = file.read_text()
	data = data.replace(search_text, replace_text)
	file.write_text(data)
	return "Text replaced"

search_text = 'AGENT'
replace_text = 'A'
print(replace_text(search_text, replace_text))


replacements = {'AGENT':'A', 'CONSUMER':'C'}

def replace_text1():
	with open('C:\Python\Data\outputCaseTestData1.txt', 'r') as infile, open('C:\Python\Data\outputCaseTestData2.txt', 'w') as outfile:
		for line in infile:
			for src, target in replacements.items():
				line = line.replace(src, target)
			outfile.write(line)
'''

#This works
def remove_special_characters():
	with open(file_path, 'r') as f:
		text = f.read()
	pattern = re.sub(r"[\([{:})\]]", "", text)	
	with open('C:\Python\Data\outputCaseTestData3.txt', 'w') as my_file:
		my_file.write(pattern)


remove_special_characters()		
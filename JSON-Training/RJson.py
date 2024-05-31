import json

with open('input.json', 'r') as  json_File:
    sample_load_file = json.load(json_File)
print(sample_load_file)


#getting hold of all values in the dictionary
test = sample_load_file['customer']

#getting hold of the values
test1 = test[1].values()  
test2 = list(test1)[0]
test3 = test2[1:-1].split(",")
print(test3[1])
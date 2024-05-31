import os
import glob
import pandas as pd
# set working directory
os.chdir="‎H:\altaCart\Projects\sd_email‎"

# find all csv files in the folder
# glob is used for pattern matching -> extension = 'csv'
# save results in list -> all_filenames
extention = 'csv'
all_filenames = [i for i in glob.glob('*{}'.format(extention))]
# print(all-filenames)

# combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
# export to csv
combined_csv.to_csv("combined_csv.csv", index=False, encoding='utf-8-sig')

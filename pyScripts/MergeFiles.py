import os
import pandas as pd

path = r'H:\altaCart\Projects\sd_email'
file_list = [
    path + f for f in os.listdir(path) if f.startswith('sd_email-sign-up')]
csv_list = []
for file in sorted(file_list):
    csv_list.append(pd.read_csv(file).assign(File_Name=os.path.basname(file)))
csv_merged = pd.concat(csv_list, ignore_index=True)
csv_merged.to_csv(path + "sd_email_full.csv", index=False)

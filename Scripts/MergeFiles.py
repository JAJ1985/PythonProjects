import os
import pandas as pd

path = 'H:/AS400/OrdersJeff'
file_list = [
    path + f for f in os.listdir(path) if f.startswith('PKG')]
csv_list = []
for file in sorted(file_list):
    csv_list.append(pd.read_csv(file).assign(File_Name=os.path.basname(file)))
csv_merged = pd.concat(csv_list, ignore_index=True)
csv_merged.to_csv(path + "Orders.csv", index=False)

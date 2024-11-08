import pandas as pd
import random
import string

# Load the dataset
df = pd.read_csv(r'C:\Python\Data\CSVTestData.csv')

df

# Define a function to randomize column values

def randomize_values(col_values):
    col_values_list = list(col_values)  # convert string to list
    random.shuffle(col_values_list)
    return ''.join(col_values_list)  # convert list back to string

# Apply the function to the desired column(s)
column_to_randomize = 'Name'
df[column_to_randomize].apply(randomize_values)

df

# define function that operates on entire dataframe

def randomize_values(df):
    for column in df.columns:
        if df[column].dtype == 'O':  # check if column has object dtype
            df[column] = [''.join(random.choices(string.ascii_letters + string.digits, k=10))
                          for _ in range(len(df))]  # generate a list of random strings
    return df

# apply function to dataframe

df_rand = randomize_values(df)

df_rand

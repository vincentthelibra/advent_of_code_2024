import pandas as pd
import numpy as np

df_lists = pd.read_csv('data.csv', header=None)
df_lists[[1, 2]] = df_lists[0].str.split(' ', n=1, expand=True)

df_list_a = df_lists[1].sort_values(ascending=True).reset_index(drop=True)
df_list_a = df_list_a.apply(pd.to_numeric, errors='coerce')

df_list_b = df_lists[2].sort_values(ascending=True).reset_index(drop=True)
df_list_b = df_list_b.apply(pd.to_numeric, errors='coerce')

diff = abs(df_list_a - df_list_b)

total_diff = diff.sum()

print(total_diff)

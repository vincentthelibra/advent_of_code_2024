import pandas as pd
import numpy as np


def merry_xmas():
    df_lists = pd.read_csv('./day_1/data.csv', header=None)
    df_lists[[1, 2]] = df_lists[0].str.split(' ', n=1, expand=True)

    df_list_a = df_lists[1].sort_values(ascending=True).reset_index(drop=True)

    # this turns df_list_a into a Pandas series
    df_list_a = df_list_a.apply(pd.to_numeric, errors="coerce")

    df_list_b = df_lists[2].sort_values(ascending=True).reset_index(drop=True)

    # this turns df_list_a into a Pandas series
    df_list_b = df_list_b.apply(pd.to_numeric, errors="coerce")

    diff = abs(df_list_a - df_list_b)

    print(df_list_a[0])
    print(df_list_b[0])

    total_diff = diff.sum()

    print(total_diff)

    return df_list_a, df_list_b


def part_2(df_list_a, df_list_b):
    frequency_df_a = df_list_b[df_list_b.isin(
        df_list_a)].value_counts().reset_index()

    frequency_df_a.columns = ["Element", "Frequency"]

    frequency_df_a["Similarity_Score"] = (frequency_df_a["Element"] *
                                          frequency_df_a["Frequency"])
    print(frequency_df_a.sum())


def merry_xmas():
    df_lists = pd.read_csv(".\day_1\data.csv", header=None)
    df_list_a, df_list_b = part_1(df_lists)
    part_2(df_list_a, df_list_b)


if __name__ == "__main__":
    merry_xmas()

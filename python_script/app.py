# coding: utf-8

from tools import import_data, construct_json_from_df, replace_value
from config import data_file
import pandas as pd


def main():
    df=import_data(data_file)
    dictionary = construct_json_from_df(df)
    df = replace_value(df, dictionary)
    df.to_csv('data_cleaned.csv', sep=',', encoding='utf-8')


if __name__ == '__main__':
    main()
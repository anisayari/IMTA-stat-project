# coding: utf-8

from tools import import_data, construct_json_from_df, replace_value, json_to_dict
from config import data_file, json_file
import pandas as pd


def main():
    df=import_data(data_file)
#    dictionary = construct_json_from_df(df,json_file)
    dico = json_to_dict(json_file)
    print dico
    df = replace_value(df, dico)
    df.to_csv('output/data_cleaned.csv', sep=';', encoding='utf-8',float_format = '%.12g')


if __name__ == '__main__':
    main()
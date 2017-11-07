# coding: utf-8

import pandas as pd
import json
import chardet
import codecs

def import_data(file):
    print "DATA IMPORT IN PROGRESS..."
    #with open(file, 'rb') as f:
    #    result = chardet.detect(f.readline()) #auto detect encoding
    df = pd.read_csv(file, encoding='utf8')
    print "DATA IMPORTED :)"
    return df

def replace_value(df, dictionary):
    print "REPLACE VALUE IN PROGRESS..."
    #df.replace(dictionary, regex=True, inplace=True)
    #df.columns = df.columns.str.replace()
    for key in dictionary:
        df[key] = df[key].map(dictionary[key])
    df.fillna(0, inplace=True)
    print "REPLACE VALUE DONE :)"
    return df


def construct_json_from_df(df):
    print "CONSTRUCT JSON IN PROGRESS..."
    header_list = list(df)
    #header_list = [x.encode('UTF8') for x in header_list]
    header_list.remove('Horodateur')
    dataframe_dict = { header : {} for header in header_list }
    for key in dataframe_dict:
        dataframe_dict[key] = { question: num for question,num in zip(df[key].unique(), range(1,len(df[key].unique())))  }
    with codecs.open('output/data_j.json', 'w', encoding="utf-8") as outfile:
        json.dump(dataframe_dict, outfile, ensure_ascii=False)
    print "CONSTRUCT JSON DONE :)"
    return dataframe_dict

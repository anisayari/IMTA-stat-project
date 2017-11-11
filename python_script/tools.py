# coding: utf-8
import pandas as pd
import json
import chardet
import codecs
import numpy as np
import math
import unicodedata

list_to_split = ['choix_serie', 'moment', 'periode', 'type_serie', 'compagnie_serie', 'avis_netflix', 'origine_serie',
                 'langue_serie', 'plateforme_serie']


def import_data(file):
    print "DATA IMPORT IN PROGRESS..."
    #with open(file, 'rb') as f:
    #    result = chardet.detect(f.readline()) #auto detect encoding
    df = pd.read_csv(file, encoding='utf8')
    print "DATA IMPORTED :)"
    return df

def json_to_dict(f):
    json1_file = open(f)
    json1_str = json1_file.read()
    dico = json.loads(json1_str)
    return dico

def replace_value(df, dictionary):
    print "REPLACE VALUE IN PROGRESS..."
    #df.replace(dictionary, regex=True, inplace=True)
    #df.columns = df.columns.str.replace()
    for key in dictionary:
        if key in list_to_split:
            list_complete=[]
            index = 0
            for item in df[key]:
                list_tmp = str(item).split(',')
                for key2 in dictionary[key]:
                    for n,item2 in enumerate(list_tmp):
                        if item2 == key2:
                            list_tmp[n] = dictionary[key][key2]
                        elif item2 == 'nan':
                            continue
                df.at[index,key] = list_tmp
                index = index + 1
        else:
            df[key] = df[key].map(dictionary[key])
    #df.fillna(0, inplace=True)
    print "REPLACE VALUE DONE :)"
    return df

def isNaN(num):
    return num != num

def construct_json_from_df(df,f):
    print "CONSTRUCT JSON IN PROGRESS..."
    header_list = list(df)
    #header_list = [x.encode('UTF8') for x in header_list]
    for key_split in list_to_split:
        smart_function(df,key_split)
    smart_function(df,'moment')
    dataframe_dict = { header : {} for header in header_list }
    for key in dataframe_dict:
        i=1
        list_unique = df[key].unique()
        for key_unique in list_unique :
            if type(key_unique) == unicode:
                key_unique = key_unique.encode('ascii','ignore')
            if isinstance(key_unique, np.float64) or isinstance(key_unique, np.float) or isinstance(key_unique, np.int):
                if np.isnan(key_unique):
                    value = 0
                    continue
                elif isinstance(key_unique, np.float64) or isinstance(key_unique, np.int) or isinstance(key_unique, np.float):
                    value = key_unique
            else:
                if key_unique == 'NaN':
                    continue
                value=i
                i= i + 1
            dataframe_dict[key][key_unique] = value
    with codecs.open(f, 'w', encoding="utf-8") as outfile:
        json.dump(dataframe_dict, outfile, ensure_ascii=False)
    print "CONSTRUCT JSON DONE :)"
    return dataframe_dict

def smart_function(df, key):
    list_complete = []
    a = df['age'].tolist()
    for item in df[key]:
        a = str(item).split(',')
        for item_tmp in a:
            if item_tmp not in list_complete:
                if item_tmp == 'nan':
                    continue
                list_complete.append(item_tmp)
    len_dict = len(df[key])
    for i in range(len(list_complete),len_dict):
        list_complete.append(np.nan)
    df[key] = list_complete
    return df
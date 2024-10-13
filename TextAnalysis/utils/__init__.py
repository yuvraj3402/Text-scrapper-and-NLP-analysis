import pandas as pd
import os,sys
from TextAnalysis.exception import ProjectException
from TextAnalysis.logger import logging
import yaml

import re
import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('punkt')
from nltk.tokenize import word_tokenize
nltk.download('wordnet')





def read_exceel_data(file_path):
    try:
        df=pd.read_excel(file_path)
        return df
    except Exception as e:
        raise ProjectException(e,sys) from e
    

def read_yaml_file(file_path):
    try:
        with open(file_path,"rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise ProjectException(e,sys) from e


def read_masterdict_folder_files(dir_path):
    try:
        list_of_dicts=[]
        for files in os.listdir(dir_path):
            file_path=os.path.join(dir_path,files)
            file = open(file_path,"r", encoding = "ISO-8859-1")
            file_content=file.read()
            file_content=file_content.splitlines()
            list_of_dicts.append(file_content)

        return list_of_dicts

    except Exception as e:
        raise ProjectException(e,sys) from e
    

def read_stopwrods_folder_files(dir_path):
    try:
        for files in os.listdir(dir_path):
            file_path=os.path.join(dir_path,files)
            file = open(file_path,"r", encoding = "ISO-8859-1")
            file_content=file.read()
            file_content=file_content.splitlines()

        return file_content

    except Exception as e:
        raise ProjectException(e,sys) from e


def lemmatize_corpus(data_frame,stop_words_list):
    try:
        lem=WordNetLemmatizer()

        corpus=[]
        for i in range(len(data_frame)):
            review=re.sub('[^a-zA-Z]',' ',data_frame["article_content"][i]).strip()
            review=review.lower()
            token=word_tokenize(review)

            review = [lem.lemmatize(word) for word in token if word not in stop_words_list]
            corpus.append(review)

        return corpus
           
    except Exception as e:
        raise ProjectException(e,sys) from e     


def count_word_syllables(word):
    try:
        vowels = "aeiouy"
        exceptions = ["es", "ed"]
        count = 0
        previous_char_was_vowel = False
        for exception in exceptions:
            if word.endswith(exception):
                return 0  
        for char in word.lower():
            if char in vowels:
                if not previous_char_was_vowel:
                    count += 1
                previous_char_was_vowel = True
            else:
                previous_char_was_vowel = False
        return count
    except Exception as e:
        raise ProjectException(e,sys) from e
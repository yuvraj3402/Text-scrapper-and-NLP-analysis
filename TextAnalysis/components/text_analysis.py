import nltk
from TextAnalysis.entity import DataIngestionArtifact,TextAnalyseArtifact
from TextAnalysis.components.data_ingestion import DataIngestion
import os,sys
from TextAnalysis.exception import ProjectException
from TextAnalysis.logger import logging
from TextAnalysis.utils import read_masterdict_folder_files,read_stopwrods_folder_files,lemmatize_corpus
from TextAnalysis.entity import *
import pandas as pd

class AnalyseText:

    def __init__(self,master_dict_config:MasterDictConfig,
                 stop_words_config:StopWordsConfig,
                 data_ingestion_artifact:DataIngestionArtifact) -> None:
        try:
            logging.info("----------------------------------------------------Starting Text Analysis----------------------------------------------------")
            self.data_ingestion_artifact=data_ingestion_artifact.new_datset
            self.master_dict_config=master_dict_config.master_dict_dir_path
            self.stop_words_config=stop_words_config.stop_words_dir_path
        except Exception as e:
            raise ProjectException(e,sys) from e



    def get_master_dict(self):
        try:
            logging.info("Get Master Dict")
            master_dict_list=read_masterdict_folder_files(dir_path=self.master_dict_config)

            neg_words_list=master_dict_list[0]
            pos_words_list=master_dict_list[1]

            logging.info("Returning neg_words_list and pos_words_list")
            return neg_words_list,pos_words_list
        except Exception as e:
            raise ProjectException(e,sys) from e


    def get_stop_words(self):
        try:
            logging.info("Get Stop Words Dict")
            stop_words_list=read_stopwrods_folder_files(dir_path=self.stop_words_config)

            logging.info("Returning Stop Words List")
            return stop_words_list
        except Exception as e:
            raise ProjectException(e,sys) from e

    
    def start_text_lemmatization(self)->TextAnalyseArtifact:
        try:


            neg_words_list,pos_words_list=self.get_master_dict()

            df=self.data_ingestion_artifact
            stop_words=self.get_stop_words()


            logging.info("Start Lemmatization of article")
            corpus=lemmatize_corpus(data_frame=df,
                             stop_words_list=stop_words)
            
            text_analyse_artifact=TextAnalyseArtifact(corpus=corpus,
                                                      neg_words_list=neg_words_list,
                                                      pos_words_list=pos_words_list)
            
            logging.info("Return Text analysis artifact")
            return text_analyse_artifact
            
        except Exception as e:
            raise ProjectException(e,sys) from e
        



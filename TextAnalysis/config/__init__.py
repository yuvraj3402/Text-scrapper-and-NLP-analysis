from TextAnalysis.exception import ProjectException
from TextAnalysis.logger import logging
from TextAnalysis.constants import *
import os,sys
from TextAnalysis.entity import *
from TextAnalysis.utils import read_yaml_file

class configuration:


    def __init__(self,confif_file_path=COFIG_FILE_PATH) -> None:
        try:
            logging.info("Reading config file")
            self.confif_file_path=read_yaml_file(file_path=confif_file_path)
            self.output_dir=self.get_pipeline_config()
        except Exception as e:
            raise ProjectException(e,sys) from e
        


    logging.info("Starting Data Ingestion Config")
    def get_data_ingestion_config(self)->DataIngestionConfig:
        try:
            logging.info("getting Data Ingestion Config Info")
            data_ingestion_info=self.confif_file_path[DATA_INGESTION_CONFIG_KEY]


            logging.info("getting Dataset File Path")
            dataset_file_path=os.path.join(data_ingestion_info[INPUT_FILE_NAME_KEY])
            
            data_ingestion_config=DataIngestionConfig(dataset_file_path=dataset_file_path)
            
            return data_ingestion_config
        except Exception as e:
            raise ProjectException(e,sys) from e



    logging.info("Getting Master Dictionary Information")
    def get_master_dict_dir_config(self)->MasterDictConfig:
        try:
            master_dict_info=self.confif_file_path[MASTER_DICT_CONFIG_KEY]

            logging.info("Getting Master Dictionary Path")
            master_dict_dir_path=os.path.join(ROOT_DIR,
                                               master_dict_info[MASTER_DICT_DIR_KEY])

            master_dict_dir_config=MasterDictConfig(master_dict_dir_path=master_dict_dir_path)

            logging.info("Returning Master Dictionary config")
            return master_dict_dir_config
        except Exception as e:
            raise ProjectException(e,sys) from e
        

    logging.info("Getting Stop Words Information")
    def get_stop_words_dir_config(self)->StopWordsConfig:
        try:

            stop_words_info=self.confif_file_path[STOP_WORDS_CONFIG_KEY]


            logging.info("Getting Stop Words Path")
            stop_words_dir_path=os.path.join(ROOT_DIR,
                                               stop_words_info[STOP_WORDS_DIR_KEY])

            stop_words_dir_config=StopWordsConfig(stop_words_dir_path=stop_words_dir_path)

            logging.info("Returning Stop Words config")
            return stop_words_dir_config

        except Exception as e:
            raise ProjectException(e,sys) from e




    logging.info("Getting Output Dirs Information")
    def get_pipeline_config(self)->OutputConfig:
            try:
                pipeline_info=self.confif_file_path[TRAINING_PIPELINE_CONFIG_KEY]



                logging.info("Getting Output Dir Path")
                output_dir=os.path.join(ROOT_DIR,
                                        pipeline_info[OUTPUT_DIR_KEY])



                logging.info("Getting Output file Path")
                output_file=os.path.join(output_dir,
                                         pipeline_info[OUTPUT_FILE_KEY])
                


                logging.info("Getting Article Folder Dir Path")
                article_folder_dir=os.path.join(output_dir,
                                                pipeline_info[ARTICLE_FOLDER_DIR_KEY])


                
                logging.info("Returning OutputDir config")
                output_config=OutputConfig(output_dir=output_dir,
                                           output_file=output_file,
                                           article_folder_dir=article_folder_dir)


                return output_config
            except Exception as e:
                raise ProjectException(e,sys) from e
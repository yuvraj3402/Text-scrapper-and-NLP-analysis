from TextAnalysis.config import configuration
from TextAnalysis.components.data_ingestion import DataIngestion
from TextAnalysis.components.text_analysis import AnalyseText
from TextAnalysis.components.generate_variables import GenerateVariables
from TextAnalysis.exception import ProjectException
from TextAnalysis.logger import logging
import os,sys

class Pipeline:


    def __init__(self,configuration=configuration()) -> None:

        logging.info("----------------------------------------------------Starting Pipeline----------------------------------------------------")
        self.configuration=configuration


    logging.info("Initializing Data Ingestion Artifact")
    def get_data_ingestion_artifact(self):
        try:
            output_config=self.configuration.get_pipeline_config()
            data_ingestion_config=self.configuration.get_data_ingestion_config()

            data_ingestion_object=DataIngestion(data_ingestion_config=data_ingestion_config,
                                                output_config=output_config)
            
            return data_ingestion_object
        except Exception as e:
            raise ProjectException(e,sys) from e
        


    logging.info("Initializing Text Analysis Artifact")
    def get_text_analysis_artifact(self,data_ingestion_artifact):
        try:
            master_dict_dir_config=self.configuration.get_master_dict_dir_config()
            stop_words_dir_config=self.configuration.get_stop_words_dir_config()

            data_ingestion_artifact=data_ingestion_artifact

            text_analysis_object=AnalyseText(master_dict_config=master_dict_dir_config,
                                              stop_words_config=stop_words_dir_config,
                                              data_ingestion_artifact=data_ingestion_artifact)
            
            return text_analysis_object
        except Exception as e:
            raise ProjectException(e,sys) from e
        


    logging.info("Initializing Generate Variable Artifact")
    def get_generate_variable_artifact(self,
                                       text_analyse_artifact,
                                       data_ingestion_artifact):
        try:

            output_config=self.configuration.get_pipeline_config()
            text_analyse_artifact=text_analyse_artifact
            data_ingestion_artifact=data_ingestion_artifact
            text_analysis_object=GenerateVariables(text_analyse_artifact=text_analyse_artifact,
                                                   data_ingestion_artifact=data_ingestion_artifact,
                                                   output_config=output_config)
                        
            return text_analysis_object
        except Exception as e:
            raise ProjectException(e,sys) from e
        



    logging.info("Initializing Pipeline")
    def start_pipeline(self):
        try:
           
           data_ingestion_object=self.get_data_ingestion_artifact()
           data_ingestion_artifact=data_ingestion_object.start_data_ingestion()


           text_analysis_object=self.get_text_analysis_artifact(data_ingestion_artifact=data_ingestion_artifact)
           text_analysis_artifact=text_analysis_object.start_text_lemmatization()

           generate_variable_object=self.get_generate_variable_artifact(text_analyse_artifact=text_analysis_artifact,
                                                                        data_ingestion_artifact=data_ingestion_artifact)
           
           generate_variable_object.generate_variables()

        except Exception as e:
            raise ProjectException(e,sys) from e
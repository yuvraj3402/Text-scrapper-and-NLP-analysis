from TextAnalysis.exception import ProjectException
from TextAnalysis.logger import logging
import os,sys
import requests
from bs4 import BeautifulSoup as bs
from TextAnalysis.constants import *
from TextAnalysis.utils import read_exceel_data
from TextAnalysis.entity import DataIngestionConfig,OutputConfig,DataIngestionArtifact
import pandas as pd


class DataIngestion:

    def __init__(self,
                 data_ingestion_config:DataIngestionConfig,
                 output_config:OutputConfig) -> None:
        
        logging.info("----------------------------------------------------Starting Data Ingestion----------------------------------------------------")
        self.data_ingestion_config=data_ingestion_config
        self.output_config=output_config
        self.new_df_list=[]
        self.article_content_list=[]





    def get_input_data_path(self):
        try:
            data_file_path=self.data_ingestion_config.dataset_file_path

            return data_file_path
        except Exception as e:
            raise ProjectException(e,sys) from e
        


    def get_data(self):
        try:
            file_path=self.get_input_data_path()
            

            logging.info("Reading input data from excel file")
            df=read_exceel_data(file_path=file_path)

            return df
        except Exception as e:
            raise ProjectException(e,sys) from e
        



    def scrap_data(self):
        try:
            df=self.get_data()

            logging.info("Scrap Data from URL files")
            for URL_IDs,URLs in zip(df[URL_ID],df[URL]):

                url_response=requests.get(URLs)

                soup=bs(url_response.text,'html.parser')
                page_title=soup.find('title').text
                text_div_classes = soup.find("div", class_="td-post-content tagdiv-type")


                texts=text_div_classes.get_text(strip=True,separator="\n").splitlines()



                new_dataframe_dict={URL_ID: URL_IDs,
                    URL : URLs,
                    ARTICLE_CONTENT:f"{page_title}-{texts}"
                }   

                self.new_df_list.append(new_dataframe_dict)




                new_article_dict={ARTICLE_CONTENT:f"{page_title}-{texts}"}
                self.article_content_list.append(new_article_dict)

                article_df=pd.DataFrame(self.article_content_list)

                article_df_folder_path=self.output_config.article_folder_dir
                os.makedirs(article_df_folder_path,exist_ok=True)


                article_df_file_path=os.path.join(article_df_folder_path,
                                                  f"{URL_IDs}.xlsx")
                article_df.to_excel(article_df_file_path,index=False)

                self.article_content_list.clear()




                                
 


            
        except Exception as e:
            raise ProjectException(e,sys) from e
        




    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            scraped_data=self.scrap_data()

            new_df=pd.DataFrame(self.new_df_list)

            logging.info("Creating Output Dir")
            os.makedirs(self.output_config.output_dir,exist_ok=True)

            output_file_path=self.output_config.output_file

            new_df.to_excel(output_file_path,index=False)

           
            dat_ingestion_artifact=DataIngestionArtifact(new_datset=new_df)
            
            logging.info("Returning data ingestion artifact")
            return dat_ingestion_artifact
        

        
        except Exception as e:
            raise ProjectException(e,sys) from e

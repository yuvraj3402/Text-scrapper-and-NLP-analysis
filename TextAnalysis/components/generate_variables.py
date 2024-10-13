from TextAnalysis.exception import ProjectException
from TextAnalysis.logger import logging
import os,sys

from TextAnalysis.components.text_analysis import AnalyseText
from TextAnalysis.entity import TextAnalyseArtifact,DataIngestionArtifact,OutputConfig
from nltk.tokenize import sent_tokenize
import pandas as pd
from TextAnalysis.utils import count_word_syllables

from TextAnalysis.constants import *

class GenerateVariables:


    def __init__(self,text_analyse_artifact:TextAnalyseArtifact,
                 data_ingestion_artifact:DataIngestionArtifact,
                 output_config:OutputConfig) -> None:

        logging.info("----------------------------------------------------Starting Generating Variables----------------------------------------------------")
        self.text_analyse_artifact=text_analyse_artifact
        self.data_ingestion_artifact=data_ingestion_artifact
        self.output_config=output_config






    def count_personal_pronouns(self,corpus):
        try:
            list_of_personal_pronouns = ['I', 'we', 'my' ,'ours','us' ]
            pronoun_counts = 0
            for words in corpus:
                if words in list_of_personal_pronouns:
                    pronoun_counts += 1
            return pronoun_counts
        except Exception as e:
            raise ProjectException(e,sys) from e







    logging.info("generating variables")
    def generate_variables(self):
        try:


            neg_word_dict=self.text_analyse_artifact.neg_words_list
            pos_word_dict=self.text_analyse_artifact.pos_words_list
            corpus_list=self.text_analyse_artifact.corpus
            dataset=self.data_ingestion_artifact.new_datset

            updated_dataframe=[]

            updated_variable_dict=[]

            k=0




            for corpus in corpus_list:


                # 1 
                positive_words_dict=[]
                for words in corpus:
                    if words in pos_word_dict:
                        positive_words_dict.append(words)
                positive_score=len(positive_words_dict)


                # 2
                negative_words_dict=[]
                for words in corpus:
                    if words in neg_word_dict:
                        negative_words_dict.append(words)
                negative_score=len(negative_words_dict)




                # 3 
                polarity_score=(positive_score - negative_score)/((positive_score + negative_score) + 0.000001)



                # 4 
                subjectivity_score = (positive_score + negative_score)/ ((len(corpus)) + 0.000001)



                variable_dict = {POSITIVE_SCORE: positive_score,
                    NEGATIVE_SCORE: negative_score,
                    POLARITY_SCORE:polarity_score,
                    SUBJECTIVITY_SCORE:subjectivity_score}
                
                updated_dataframe.append(variable_dict)
            




            for article in dataset[ARTICLE_CONTENT]:
                texts=corpus_list[k]
                
                # 5
                average_sentence_length=round(len(texts)/len(sent_tokenize(article)))


                # 6
                num_complex_words = sum(1 for text in texts if count_word_syllables(text) >= 2)
                percentage_complex_words = round((num_complex_words / len(texts)) * 100,1)



                # 7
                fog_index = 0.4*(average_sentence_length + percentage_complex_words)



                # 8 
                average_number_of_words_per_sentence=round(len(texts)/len(sent_tokenize(article)),1)



                # 9
                total_num_of_complex_words_count=num_complex_words
            
            

                # 10
                word_count = len(texts)



                # 11
                syllables_per_word ={word: count_word_syllables(word) for word in texts}



                # 12
                personal_pronouns=self.count_personal_pronouns(texts)


                
                # 13
                word_sum=sum([len(i) for i in texts])



                # 14
                avg_words=round(word_sum/len(texts),1)





                variable_dict = {AVERAGE_SENTENCE_LENGTH: average_sentence_length,
                                PERCENTAGE_OF_COMPLEX_WORDS: f"{percentage_complex_words} %",
                                FOG_INDEX:fog_index,
                                AVG_NUMBER_OF_WORDS_PER_SENTENCE:average_number_of_words_per_sentence,
                                COMPLEX_WORDS_COUNT:total_num_of_complex_words_count,
                                WORD_COUNT:word_count,
                                SYLLABLE_PER_WORD:syllables_per_word,
                                PERSONAL_PRONOUNS:personal_pronouns,
                                AVG_WORDS:avg_words}
                

                updated_variable_dict.append(variable_dict)
                k+=1


            
            

            dataset2=pd.DataFrame(updated_dataframe)
            dataset3=pd.DataFrame(updated_variable_dict)
            updated_dataframe=pd.concat([dataset,dataset2,dataset3],axis=1)



            logging.info("Returning generated variables")
            updated_dataframe=updated_dataframe.drop(ARTICLE_CONTENT,axis=1)

            logging.info("Saving dataframe to the excel file")
            updated_dataframe.to_excel(self.output_config.output_file,index=False)



        except Exception as e:
            raise ProjectException(e,sys) from e




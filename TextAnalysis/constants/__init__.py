import os

ROOT_DIR=os.getcwd()


CONFIG_DIR="config"
CONFIG_FILE_NAME="config.yaml"

COFIG_FILE_PATH=os.path.join(ROOT_DIR,CONFIG_DIR,CONFIG_FILE_NAME)


#pipeline constants
TRAINING_PIPELINE_CONFIG_KEY = "training_pipeline_config"
OUTPUT_DIR_KEY = "output_dir"
OUTPUT_FILE_KEY="output_file"
ARTICLE_FOLDER_DIR_KEY="article_folder_dir"


#data ingestion constants
DATA_INGESTION_CONFIG_KEY = "data_ingestion_config"
INPUT_FILE_NAME_KEY = "input_file_name"


#dataframe constants
URL="URL"
URL_ID="URL_ID"
ARTICLE_CONTENT="article_content"



#master dict dir constants
MASTER_DICT_CONFIG_KEY="master_dict_config"
MASTER_DICT_DIR_KEY="master_dict_dir_name"


#stop words dir constants
STOP_WORDS_CONFIG_KEY="stop_words_config"
STOP_WORDS_DIR_KEY="stop_words_dir_name"



#variable constants
POSITIVE_SCORE="POSITIVE SCORE"
NEGATIVE_SCORE="NEGATIVE SCORE"
POLARITY_SCORE="POLARITY SCORE"
SUBJECTIVITY_SCORE="SUBJECTIVITY SCORE"
AVERAGE_SENTENCE_LENGTH="AVERAGE SENTENCE LENGTH"
PERCENTAGE_OF_COMPLEX_WORDS ="PERCENTAGE OF COMPLEX WORDS"
FOG_INDEX="FOG INDEX"
AVG_NUMBER_OF_WORDS_PER_SENTENCE="AVG NUMBER OF WORDS PER SENTENCE"
COMPLEX_WORDS_COUNT="COMPLEX WORD COUNT"
WORD_COUNT="WORD COUNT"
SYLLABLE_PER_WORD="SYLLABLE PER WORD"
PERSONAL_PRONOUNS="PERSONAL PRONOUNS"
AVG_WORDS="AVG WORD LENGTH"

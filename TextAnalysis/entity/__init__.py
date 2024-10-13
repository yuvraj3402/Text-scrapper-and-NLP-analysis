from collections import namedtuple


OutputConfig = namedtuple("OutputConfig", ["output_dir","output_file","article_folder_dir"])



DataIngestionConfig=namedtuple("DataIngestionConfig",["dataset_file_path"])


MasterDictConfig=namedtuple("MasterDictConfig",["master_dict_dir_path"])


StopWordsConfig=namedtuple("StopWordsConfig",["stop_words_dir_path"])





DataIngestionArtifact=namedtuple("DataIngestionArtifact",["new_datset"])


TextAnalyseArtifact=namedtuple("TextAnalyseArtifact",["corpus","neg_words_list","pos_words_list"])

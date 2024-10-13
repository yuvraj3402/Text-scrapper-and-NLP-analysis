# Data Extraction and NLP

Data Extraction and NLP is a Data Science project which extract textual data articles from given URLs and perform text analysis to compute various variables.

## Install Dependencies

All required Dependencies and required libraries are listed in **requiremnts.txt** file. To install dependencies first run

```bash
pip install -r requirements.txt
```
## Understanding Code

1. This Project is made using Modular coding and all the coded files can be found in **TextAnalysis** folder.
2. The flow of the code is first we write config.yaml file which can be found in **config** folder at the top. It contains al the basic config of the project such as Input file name ,Output directory name,Output file name etc.
3. Then inisde **TextAnalysis** folder can be found **constant** folder where we Hard code all the required Texts. We hardcode all the Key pairs of **config.yaml** file.
4. After constants we specify config and artifact entity which can be found in **entity** folder.
5. After that we code all the paths and configuration needed in **Config** Folder inside of **TextAnalysis** folder. It contains all the paths such as  output_folder path , where output.xlsx file be created and it's path.
6. After conifuration and specifying all the important file paths that are required and will be required we move on to **components** folder.
7. We first code **data_ingestion.py** file which will read our input file i.e Input.xlsx. Read the URL data using pandas library. Scrap the Article content and Article heading using beautiful soap library and store the scrapped article in the folder **article_folder** which can be found in **output_folder** a text file with URL_ID as its file . We also add this scrapped article in our new dataset wich also contains URL_ID and URL and use this dataset ahead to find various variables.
8. To read these files you can run a simple code in jupyter notebook.

```python
import pandas as pd

# paste path of the file in file_path
file_path="string"
pd.read_excel(file_path)
```

9. Then we code **text_analysis.py** , In this file we use lemmatization process which uses **StopWords** folder and removes all the stop words from the scrapped article and creates a corpus that contains all the lemmatized words. text_analysis.py file returns us a list which contains all the words after we perform lemmatization. 
10. Then we code **generate_variables.py** file in which we perform various steps to find variables asked of us.
11. after component folder we code **pipeline** folder which calls all the functions scattered around in different files. we create objects and call functions to run our project in one simple line.
12. We call **pipeline** folder file in **app.py** . To run the programe simply run the following command in your terminal. 
```bash
python app.py
```
13. Or run in jupyter notebook

```python
from TextAnalysis.pipeline import Pipeline

pipeline_object=Pipeline()

pipeline_artifact=pipeline_object.start_pipeline()


if __name__=="__main__":
    pipeline_artifact
```

14. **Utils** folder contains all the small functions that are called again and again to save space and increase code usability.
15. **Exception** folder contains custom exception code that i coded whic can give us better understanding of error when we face it.
16. **Logger** folder contains code for logging. when program is run it generates a Logs_folder which contains all the logging information of our project. It can help us pin point where our code failed.


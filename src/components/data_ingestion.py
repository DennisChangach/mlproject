#Reading the data from the source e.g database
import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    #path for data ingestion component
    raw_data_path:str=os.path.join('artifacts','data.csv')
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion component")
        try:
            #reading the csv file into a dataframe
            df = pd.read_csv('notebook\data\stud.csv')
            #logging this in the logfiles
            logging.info("Read tge dataset as a dataframe")

            #creating the artifacts folder
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            #saving the raw data
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            #Train test Split
            logging.info("Train Test split initiated")
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)

            #saving the train & test datasets
            train_set.to_csv(self.ingestion_config.train_data_path,index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of the data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)
        

if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()

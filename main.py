import sys
import os
from src.pipeline.train_pipeline import TrainPipeline
from src.components.data_ingestion import DataIngestion
from src.logger import logging
from src.exception import CustomException

#Function to ingest data
def ingest_data():
    logging.info("Started Data Ingestion Pipeline")
    try:
        ingest = DataIngestion()
        ingest.initiate_data_ingestion()

    except Exception as e:
        raise CustomException(e,sys)


#Main function to train the model
def train():
    logging.info("Starting the Training Pipeline")
    try:
        model_trainer = TrainPipeline()
        model_trainer.train_model()
    except Exception as e:
        raise CustomException(e,sys)
if __name__=="__main__":
    train()
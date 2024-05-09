from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformationConfig
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer


def main():
    obj=DataIngestion()
    train_data,test_data = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    train_arr,test_arr= data_transformation.initiate_data_transformation(train_data,test_data)

    model_trainer = ModelTrainer()
    model_trainer.initiate_model_trainer(train_array=train_arr,test_array=test_arr)

if __name__=="__main__":
    main()
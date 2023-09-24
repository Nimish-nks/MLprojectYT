from src.logger import logging
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion

from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer,ModelTrainerConfig
import sys

if __name__=="__main__":
    logging.info('The execution has started')

try:
    #daa ingestion  
    obj=DataIngestion()
    train_data_path, test_data_path =obj.initiate_data_ingestion()
    #data transformation
    data_transformation = DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation( train_data_path,test_data_path)

    #model training
    model_trainer = ModelTrainer()
    print(model_trainer.initiate_model_trainer(train_arr,test_arr)) #to print R2 score

except Exception as e:
    logging.info("Custom Exception")
    raise CustomException(e,sys)

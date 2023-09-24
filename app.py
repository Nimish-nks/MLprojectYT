from src.logger import logging
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion

from src.components.data_transformation import DataTransformation

import sys


if __name__=="__main__":
    logging.info('The execution has started')

try:
        
    obj=DataIngestion()
    train_data_path, test_data_path =obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation( train_data_path,test_data_path)

except Exception as e:
    logging.info("Custom Exception")
    raise CustomException(e,sys)
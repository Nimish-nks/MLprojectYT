from src.logger import logging
from src.exception import CustomException
import sys
from src.components.data_ingestion import DataIngestion
#from src.components.data_ingestion import DataIngestionConfig


if __name__=="__main__":
    logging.info('The execution has started')

try:
    #data_ingestion_config = DataIngestionConfig()
    data_ingestion = DataIngestion()
except Exception as e:
    logging.info("Custom Exception")
    raise CustomException(e,sys)
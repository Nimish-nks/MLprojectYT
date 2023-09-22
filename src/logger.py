import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  #will create log file with name using datetime and extension log
log_path=os.path.join(os.getcwd(),"logs",LOG_FILE)  #it will make folder logs and store log file there
os.makedirs(log_path,exist_ok=True)  #If folder there already so skip it

LOG_FILE_PATH=os.path.join(log_path,LOG_FILE)  #you have made log file path

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,

)
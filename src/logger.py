#Logging all the information that occurs
import logging
import os
from datetime import datetime

#creating the LOG FILE
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
#getcwd - current working dir
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
#create log dir -exist_ok=True - appends the file to the folder
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,

)

if __name__=="__main__":
    logging.info("Logging has started")
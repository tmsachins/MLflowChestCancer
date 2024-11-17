import logging

# Configure the root logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Get the root logger
logger = logging.getLogger()

# Log messages
# logger.debug("This is a DEBUG message.")  # Won't appear (INFO level is higher)
# logger.info("This is an INFO message.")   # Will appear
# logger.warning("This is a WARNING message.")  # Will appear
logger.debug("This is a debug message.")
logger.info("This is an info message.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")
logger.critical("This is a critical message.")



import os
import sys


logging_str = "%(levelname)s: %(module)s : line no> %(lineno)d : %(message)s"

log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger2 = logging.getLogger("cnnClassifierLogger1")


logger2.info("Welcome to cnnClassifier")
# 'print(str(logging.basicConfig))
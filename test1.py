import logging

# Configure basic logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s-%(lineno)d - %(message)s')

logging.basicConfig(level=logging.INFO,format="%(asctime)s - %(levelname)-8s - module %(module)s - %(lineno)d - %(message)s")
 
# Example usage
logging.debug("This is a debug message.")
logging.info("This is an info message.")
logging.warning("This is a warning message.")
logging.error("This is an error message.")
logging.critical("This is a critical message.")


import os
import sys
import logging

logging_str = "[%(levelname)s: %(module)s:%(lineno)d: %(message)s]"

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

logger = logging.getLogger("cnnClassifierLogger1")


logger.info("Welcome to cnnClassifier")
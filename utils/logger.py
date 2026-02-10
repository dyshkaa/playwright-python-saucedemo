import logging
import os
import sys

def setup_logger(name="test_logger", log_file="test_run.log"):
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO) 

    if logger.hasHandlers():
        logger.handlers.clear()

    formatter = logging.Formatter('[%(asctime)s] [%(processName)s] [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    file_path = os.path.join(log_dir, log_file)
    file_handler = logging.FileHandler(file_path, encoding='utf-8')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger
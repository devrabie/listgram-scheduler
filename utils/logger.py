import logging

def setup_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler("logs/app.log")
    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger

logger = setup_logger(__name__)
def log_message(message):
    logger.info(message)
def log_error(message):
    logger.error(message)
def log_warning(message):
    logger.warning(message)
def log_debug(message):
    logger.debug(message)
def log_critical(message):
    logger.critical(message)
def log_exception(message):
    logger.exception(message)
def log_info(message):
    logger.info(message)
def log_success(message):
    logger.info(message)

import logging


def get_logger():
    logging.basicConfig(filename='test.log', encoding='utf')
    logger = logging.Logger
    return logger


# Simple logging function for server output
def log(level, msg, file_name):
    if level == 'INFO':
        get_logger().log(level=logging.INFO, msg=msg)



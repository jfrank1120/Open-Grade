import logging


def get_logger():
    logging.basicConfig(filename="test.log", encoding='utf-8')
    logger = logging.Logger
    return logger


# Simple logging function for server output
def log(msg, file_name):
    print(file_name + ": " + msg)


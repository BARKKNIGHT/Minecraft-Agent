import logging
# import mylib
logger = logging.getLogger(__name__)

class Logger:
    def __init__(self,file_name='mylog.log'):
        """Init logger file name and create a logger object"""
        logging.basicConfig(filename=file_name, level=logging.INFO)
        logger = logging.getLogger(__name__)

    def log_info(self,log_info):
        """Save logs_info to a file"""
        self.logger.info(log_info)


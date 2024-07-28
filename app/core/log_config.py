import logging
import os
from datetime import datetime
import pytz

class TaiwanFormatter(logging.Formatter):
    def formatTime(self, record, datefmt=None):
        dt = datetime.fromtimestamp(record.created, pytz.timezone('Asia/Taipei'))
        if datefmt:
            return dt.strftime(datefmt)
        else:
            return dt.isoformat()

class Logger:
    def __init__(self, log_dir='.log', log_file='application.log', logger_name='my_logger'):
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.INFO)

        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        formatter = TaiwanFormatter("%(asctime)s %(levelname)s %(message)s")
        self.add_stream_handler(formatter)
        self.add_file_handler(log_dir, log_file, formatter)

    def add_stream_handler(self, formatter):
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

    def add_file_handler(self, log_dir, log_file, formatter):
        fh = logging.FileHandler(os.path.join(log_dir, log_file))
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)

    def add_filter(self, filter_func):
        self.logger.addFilter(filter_func)

    def get_logger(self):
        return self.logger
    
# def logging_setting():
#     if LOGGING_LEVEL == 1:
#         logging.basicConfig(level=logging.ERROR)
#     elif LOGGING_LEVEL == 2:
#         logging.basicConfig(level=logging.WARNING)
#     elif LOGGING_LEVEL == 3:
#         logging.basicConfig(level=logging.INFO)
#     elif LOGGING_LEVEL == 4:
#         logging.basicConfig(level=logging.DEBUG)
#     else:
#         logging.basicConfig(level=logging.DEBUG)

logger_instance = Logger()
logger = logger_instance.get_logger()


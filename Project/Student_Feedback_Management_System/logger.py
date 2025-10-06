# logger.py

import datetime
import os
from config import LOG_FILE
from exceptions import FileHandlingError

class Logger:
    @staticmethod
    def write_log(message):
        try:
            # Ensure the directory for the log file exists
            log_dir = os.path.dirname(LOG_FILE)
            if log_dir and not os.path.exists(log_dir):
                os.makedirs(log_dir)

            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Open the file with explicit encoding and error handling
            with open(LOG_FILE, "a", encoding="utf-8", errors="ignore") as f:
                f.write(f"[{timestamp}] {message}\n")

        except PermissionError as e:
            raise FileHandlingError(f"Permission denied when writing to log file '{LOG_FILE}': {e}")
        except Exception as e:
            raise FileHandlingError(f"Error writing to log file '{LOG_FILE}': {e}")

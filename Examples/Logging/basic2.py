import logging
 
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s | %(levelname)s | %(message)s')
 
def process_data(data):
    logger = logging.getLogger("process the data...")
    logger.debug("Processing the data : %s", data)
    return [d.upper() for d in data]

class Calculator:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
       
    def divide(self,a,b):
        self.logger.info("Dividing %d by %d", a,b)
        try:
            return a/b
        except ZeroDivisionError:
            self.logger.error("Division by zero", exc_info=True)
            return None
       
process_data(["apple","cheery"])
 
calc = Calculator()
calc.divide(10,2)
calc.divide(5,0)
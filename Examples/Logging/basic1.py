import logging
 
#logging.basicConfig(level=logging.DEBUG,format='%(asctime)s | %(levelname)s | %(name)s | %(message)s')
 
logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s')
username = "Vinay"
items = 50
 
logging.info("The username %s bought %d this may items",  username, items)



############################################################################################3


#logging.basicConfig(level=logging.DEBUG,format='%(asctime)s | %(levelname)s | %(name)s | %(message)s')
 
logging.basicConfig(level=logging.ERROR, format='%(asctime)s | %(levelname)s | %(message)s')
 
try:
  res = 10/0
except Exception as e:
    logging.error(" An error occured ", exc_info=True)
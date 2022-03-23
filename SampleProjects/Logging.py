import logging

logging.basicConfig(filename="C://Users//THADEUS ODHIAMBO//PycharmProjects//Selenium//SeleniumLogs//test.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

logging.debug("This ia a debug message")
logging.info("This ia a info message")
logging.warning("This ia a warning message")
logging.error("This ia a error message")
logging.critical("This ia a critical message")
import logging

logging.basicConfig(filename="C://Users//THADEUS ODHIAMBO//PycharmProjects//Selenium//SeleniumLogs//test.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug("This ia a debug message")
logger.info("This ia a info message")
logger.warning("This ia a warning message")
logger.error("This ia a error message")
logger.critical("This ia a critical message")
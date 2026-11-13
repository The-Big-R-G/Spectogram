import logging

#define the logger
logger = logging.getLogger('spectogram')

#set level
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()

format = '(asctime)s - %(levelname)s - %(filename)s - %(message)s'
formatter = logging.Formatter(format)
handler.setFormatter(formatter)

logger.addHandler(handler)
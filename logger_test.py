from logging import getLogger, StreamHandler, Formatter, DEBUG


# create logger and set level
logger = getLogger(__name__)
logger.setLevel(DEBUG)

# create console handle and set level
ch = StreamHandler()
ch.setLevel(DEBUG)

# create formatter
formatter = Formatter('[{asctime}] [{name}] {message}', datefmt='%Y/%m/%d %H:%M:%S', style='{')

# add formatter to ch
ch.setFormatter(formatter)

# add ch tp logger
logger.addHandler(ch)

logger.info("This info should be logged")

import logging
from fdmgmt.common import conf as cfg

CONF = cfg.CONF

MAP_LOGLEVEL = {'debug': logging.DEBUG,
                'info': logging.INFO,
                'warning': logging.WARNING,
                'error': logging.ERROR,
                'critical': logging.CRITICAL}

def getLogger(name):
    logger = logging.getLogger(name)
    logger.setLevel(MAP_LOGLEVEL[CONF['logging']['log_level']])

    # create the logging file handler
    FILEPATH = '%s/%s.log' %(CONF['logging']['log_folder'], 'fdmgmt')
    fh = logging.FileHandler(FILEPATH)
    formatter = logging.Formatter('%(asctime)s %(levelname)s '  
                                  '%(lineno)s %(name)s.%(funcName)s [-] %(message)s ')

    fh.setFormatter(formatter)
    # add handler to logger object
    logger.addHandler(fh)
    return logger

if __name__ == "__main__":
    LOG = getLogger(__name__)
    LOG.debug("A debugging message")
    LOG.info("Welcome to Logging")
    LOG.warning("A warning occurred")
    LOG.error("An error occurred")
    LOG.exception("An Exception occurred")

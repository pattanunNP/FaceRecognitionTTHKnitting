
import sys
import logging
import colorlog


class Logger(object):
    loggers = set()

    def __init__(self, name,
                 format="%(asctime)s | %(levelname)s | %(message)s",
                 level='info',
                 log_file="run.log",
                 save_to_file=True):

        # Initial construct.
        self.format = format
        self.level = level
        self.name = name
        self.levels = {
            'critical': logging.CRITICAL,
            'error': logging.ERROR,
            'warn': logging.WARNING,
            'warning': logging.WARNING,
            'info': logging.INFO,
            'debug': logging.DEBUG
        }

        self.log_file = log_file

        self.level = self.levels.get(self.level)

        # Logger configuration.
        self.console_formatter = logging.Formatter(self.format)
        self.console_logger = logging.StreamHandler(sys.stdout)
        self.console_logger.setFormatter(self.console_formatter)

        formatter = colorlog.ColoredFormatter(
            "%(log_color)s %(asctime)s %(levelname)-8s %(log_color)s %(message)s",
            datefmt=None,
            reset=True,
            log_colors={
                'DEBUG':    'cyan',
                'INFO':     'green',
                'WARNING':  'yellow',
                'ERROR':    'red',
                'CRITICAL': 'red,bg_white',
            },
            secondary_log_colors={},
            style='%'
        )
        self.console_logger.setFormatter(formatter)

        # Complete logging config.
        if save_to_file:
            logging.basicConfig(filename=log_file,
                                level=self.level,
                                format=self.format)
        self.logger = logging.getLogger(name)

        if name not in self.loggers:
            self.loggers.add(name)
            self.logger.setLevel(self.level)
            self.logger.addHandler(self.console_logger)

    def info(self, msg, extra=None):
        self.logger.info(msg, extra=extra)

    def error(self, msg, extra=None):
        self.logger.error(msg, extra=extra)

    def debug(self, msg, extra=None):
        self.logger.debug(msg, extra=extra)

    def warn(self, msg, extra=None):
        self.logger.warn(msg, extra=extra)

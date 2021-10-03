"""
__author__ = "pattanunNP"
__version__ = "0.1.0"
__license__ = "MIT"

"""

import sys
import argparse
import logging
import os
import colorlog
from engine.utils.log import Logger
from engine.pipe.Pipeline import Pipeline

parser = argparse.ArgumentParser(description='Train')


parser.add_argument('-v', '--version',
                    action='version',
                    version='%(prog)s 1.0.0a',
                    help="Show program's version number and exit.")

parser.add_argument('-d', '--directory',
                    help="image source path",
                    dest="directory",
                    type=str)

parser.add_argument('-o', '--output',
                    help="Output Path",
                    dest="output",
                    type=str)

parser.add_argument('-m', '--model',
                    help="select model [spotify-annoy/faiss]",
                    choices=['spotify', 'faiss'])


parser.add_argument('-l', '--loglevel',
                    help=(
                        "Provide logging level. "
                        "Example --log debug', default='warning'"),

                    dest="loglevel",
                    choices=['debug', 'info', 'warn', 'error', 'critical'],
                    default="info",
                    type=str)

parser.add_argument('--log-file',
                    help="File to write log to",
                    dest="log_file",
                    default="train.log")


args = parser.parse_args()


logger = Logger(name="train",
                level=args.loglevel.lower(),
                log_file=args.log_file,
                save_to_file=False)


class Train:

    def __init__(self):

        logger.info('Started Process')
        logger.debug(
            f'Args: (Dir="{args.directory}" OutputPath="{args.output}" Model={args.model})')
        self.Pipeline = Pipeline()

    def run(self, dir):
        self.Pipeline.PrepareImage(dir)


if __name__ == '__main__':
    train = Train()
    train.run(dir=args.directory)

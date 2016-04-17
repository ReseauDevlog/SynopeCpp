#!/usr/bin/env python
# -*- coding: utf-8 -*-

'Custom logging'

import os
import os.path
import sys
import logging


class VarFormatter(logging.Formatter):

    'Customized formatting for console'

    default_formatter = logging.Formatter('%(levelname)s in %(name)s: %(message)s')

    def __init__(self, formats):
        """ formats is a dict { loglevel : logformat } """
        super(VarFormatter, self).__init__()
        self.formatters = {}
        for loglevel in formats:
            self.formatters[loglevel] = logging.Formatter(formats[loglevel])

    def format(self, record):
        formatter = self.formatters.get(record.levelno, self.default_formatter)
        return formatter.format(record)


class InfoOnlyFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.INFO


console_handler = logging.StreamHandler()
console_handler.setFormatter(VarFormatter({
    logging.DEBUG: '(%(message)s)',
    logging.INFO: '%(message)s',
    logging.WARNING: 'warning: %(message)s',
    logging.ERROR: 'ERROR: %(message)s',
    logging.CRITICAL: 'CRITICAL ERROR: %(message)s',
}))
console_handler.setLevel(logging.INFO)

script_name = os.path.basename(sys.argv[0])
if script_name.endswith('.py'):
    script_name = script_name[:-3]

log_file_name = script_name+".log"
log_file_handler = logging.FileHandler(log_file_name, mode="w", encoding="utf-8")
log_file_handler.setFormatter( \
    logging.Formatter("%(asctime)s :: %(name)s :: %(levelname)-8s :: %(message)s"))
log_file_handler.setLevel(logging.DEBUG)

#out_file_name = script_name+".out"
#out_file_handler = logging.FileHandler(out_file_name, mode="w", encoding="utf-8")
#out_file_handler.setFormatter(logging.Formatter("%(message)s"))
#out_file_handler.addFilter(InfoOnlyFilter())

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(console_handler)
logger.addHandler(log_file_handler)
#logger.addHandler(out_file_handler)

def tests():
    'Unit tests'
    logging.debug('Debug message')
    logging.info('Info message')
    logging.warning('Warning message')
    logging.error('Error message')
    logging.critical('Critical message')
    return 0

if __name__ == '__main__':
    sys.exit(tests())



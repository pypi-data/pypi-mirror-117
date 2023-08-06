#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Master module for metest
"""

__author__ = "K. Hintz"
__copyright__ = "Danish Meteorological Institute"

__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "K. Hintz"
__email__ = "kah@dmi.dk"
__status__ = "Development"

import sys
import os
sys.path.insert(0, os.path.abspath('./metest/'))
import argparse
from argparse import ArgumentDefaultsHelpFormatter

from .logmetric import logmetric
from .datametric import datametric


class MyParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)


if __name__ == '__main__':
    parent_parser = MyParser(
        description='Test, check and compare logs and data from meteorological computations.',
        formatter_class=ArgumentDefaultsHelpFormatter)
    
    subparser = parent_parser.add_subparsers(dest="cmd")

    parser_logmetric = subparser.add_parser('logmetric', help='Get metrics from logfile')
    parser_datametric = subparser.add_parser('datametric', help='Get metrics from output data')

    parser_logmetric.add_argument('-m',
                    '--model',
                    metavar='MODEL',
                    type=str,
                    help='Which model are logfiles coming from (harmonie)',
                    required=True)
    
    parser_logmetric.add_argument('-c',
                    '--compare',
                    action='store_true',
                    help='Compute metrics from comparing two logfiles')

    parser_logmetric.add_argument('-i',
                    '--individual',
                    action='store_true',
                    help='Compute metrics from one logfile')

    parser_logmetric.add_argument('-f',
                    '--file',
                    metavar='FILE',
                    type=str,
                    help='Path to logfile to read',
                    required=True)

    parser_logmetric.add_argument('-f2',
                    '--file2',
                    metavar='FILE2',
                    type=str,
                    help='Path to second logfile to read',
                    required=False)


    if len(sys.argv)==1:
        parent_parser.print_help()
        sys.exit(2)

    args = parent_parser.parse_args()

    if args.cmd == 'logmetric':
        logwork = logmetric(args)

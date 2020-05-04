#!/usr/bin/env python3
"""
Author : MK
Date   : 20.05.04
Purpose: CSV filter
"""

import argparse
import csv
import re
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Filter delimited records',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        required=True,
                        default=None)

    parser.add_argument('-v',
                        '--val',
                        help='Value for filter',
                        metavar='val',
                        type=str,
                        required=True,
                        default=None)

    parser.add_argument('-c',
                        '--col',
                        help='Column for filter',
                        metavar='col',
                        type=str,
                        default='')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='OUTFILE',
                        type=argparse.FileType('wt'),
                        default='out.csv')

    parser.add_argument('-d',
                        '--delimiter',
                        help='Input file',
                        metavar='delim',
                        type=str,
                        default=',')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    reader = csv.DictReader(args.file, delimiter=args.delimiter)

    for row in reader:
        for column, value in row.items():
            if value is None or value == "":
                parser.error(f'--col "{args.col}" not a valid column!')

    writer = csv.DictWriter(args.outfile, fieldnames=reader.fieldnames)
    writer.writeheader()

    for rec in reader
        if re.search(search_for, text, re.IGNORECASE)
            writer
        print(rec)
        break






# --------------------------------------------------
if __name__ == '__main__':
    main()

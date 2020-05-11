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
                        help='Delimiter',
                        metavar='delim',
                        type=str,
                        default=',')

    args = parser.parse_args()

    # if
    #     parser.error(f'')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    reader = csv.DictReader(args.file, delimiter=args.delimiter)

    if args.col:
        if args.col in reader.fieldnames:
            pass
        else:
            die(f'--col "{args.col}" not a valid column!')

    writer = csv.DictWriter(args.outfile, fieldnames=reader.fieldnames)
    writer.writeheader()

    num_write = 0
    for rec in reader:
        text = str(rec.get(args.col)) if args.col else str(rec)
        if re.search(args.val, text, re.IGNORECASE):
            writer.writerow(rec)
            num_write += 1

    print(f'Done, wrote {num_write} to "{args.outfile.name}".')

# --------------------------------------------------
def die(msg):
    """Print message to STDERR and exit with an error"""
    print(msg, file=sys.stderr)
    sys.exit(1)

# --------------------------------------------------
if __name__ == '__main__':
    main()

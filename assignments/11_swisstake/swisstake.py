#!/usr/bin/env python3
"""
Author : MK
Date   : 20.04.29
Purpose: Filter SwissProt file for keywords, taxa
"""

import argparse
from Bio import SeqIO
import re
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Filter SwissProt file for keywords, taxa',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE',
                        help='SwissProt file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default=None)

    parser.add_argument('-k',
                        '--keyword',
                        help='Keyword to take',
                        metavar='keyword',
                        type=str,
                        nargs='+',
                        required=True,
                        default=None)

    parser.add_argument('-s',
                        '--skiptaxa',
                        help='Taxa to skip',
                        metavar='[taxa [taxa ...]]',
                        type=str,
                        default=None)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='out.fa')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for rec in SeqIO.parse(args.file, "swiss"):
        print(rec)
        taxa = set(map(str.lower, args.file))
        skip = set(map(str.lower, args.skiptaxa))
        if skip.intersection(taxa):
            pass
        if

    print(f'Done, skipped {} and took {}. See output in "{args.outfile.name}')


# --------------------------------------------------
if __name__ == '__main__':
    main()

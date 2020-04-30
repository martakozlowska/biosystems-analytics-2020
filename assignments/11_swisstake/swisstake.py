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
    #want_key = set([key.lower() for key in args.keyword)
    want_key = set(map(str.lower, args.keyword))
    skip_taxa = set(map(str.lower, args.skiptaxa or []))

    for rec in SeqIO.parse(args.FILE, "swiss"):
        annot = rec.annotations
        keywords = annot.get('keywords')
        num_take, num_skip = 0, 0
        if keywords:
            keywords = set(map(str.lower, keywords))
            if want_key.intersection(keywords):
                num_take += 1
                SeqIO.write(rec, args.outfile, 'fasta')
        taxa = annot.get('taxonomy')
        if taxa:
            taxa = set(map(str.lower, taxa))
            if skip_taxa.intersection(taxa):
                num_skip += 1
                continue
        break


    print(f'Done, skipped {num_skip} and took {num_take}. See output in "{args.outfile.name}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()

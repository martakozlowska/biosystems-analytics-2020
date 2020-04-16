#!/usr/bin/env python3
"""
Author : MK
Date   : 20.04.14
Purpose: Unclustered proteins
"""

import argparse
import re
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find proteins not clustered by CD-HIT',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-c',
                        '--cdhit',
                        help='Output file from CD-HIT (clustered proteins)',
                        metavar='cdhit',
                        type=argparse.FileType('r'),
                        required=True,
                        default=None)

    parser.add_argument('-p',
                        '--proteins',
                        help='Proteins FASTA',
                        metavar='proteins',
                        type=argparse.FileType('r'),
                        required=True,
                        default=None)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='outfile',
                        type=str,
                        default='unclustered.fa')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    protein_ids = set()
    for line in args.cdhit:
        match = re.search(r'>(\d+', line)
        id = match.group()
        protein_ids.add(id)

    for line in args.cdhit:
        re.sub(r'\|.*','', line)

# --------------------------------------------------
if __name__ == '__main__':
    main()

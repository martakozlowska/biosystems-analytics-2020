#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""

import argparse
import os
import sys
import random
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Sample',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input FASTA file(s)',
                        metavar='file',
                        nargs='+',
                        type=argparse.FileType('r'),
                        default=None)

    parser.add_argument('-p',
                        '--pct',
                        help='Percent of reads',
                        metavar='reads',
                        type=float,
                        default=0.1)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed value',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory',
                        metavar='DIR',
                        type=str,
                        default='out')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    out_dir = args.outdir

    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)

    num = 0
    for fh in args.file:
        basename = os.path.basename(fh.name)
        out_file = os.path.join(out_dir, basename)
        num += 1
        print(f'{num}: {basename}')

        """
        out_fh = 
        for rec in SeqIO.parse(fh, 'fasta'):
            if:
                SeqIO.write(rec, out_fh, 'fasta')
                
        out_fh.close()
        """

    print(f'Wrote sequences from files to directory "basename"')



# --------------------------------------------------
if __name__ == '__main__':
    main()

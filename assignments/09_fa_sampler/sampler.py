#!/usr/bin/env python3
"""
Author : MK
Date   : 2020.04.07
Purpose: sample
"""

import argparse
import os
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

    args = parser.parse_args()

    if not 0 < args.pct < 1:
        parser.error(f'--pct "{args.pct}" must be between 0 and 1')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    out_dir = args.outdir

    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)

    num_files = 0
    num_seq = 0
    total_seq = 0

    for fh in args.file:
        basename = os.path.basename(fh.name)
        out_file = os.path.join(out_dir, basename)
        num_files += 1
        print(f'  {num_files}: {basename}')

        out_fh = open(out_file, 'wt')
        for rec in SeqIO.parse(fh, 'fasta'):

            if random.random() <= args.pct:
                SeqIO.write(rec, out_fh, 'fasta')
                num_seq += 1

        out_fh.close()

    total_seq += num_seq
    s = 's' if num_files > 1 else ''

    print(f'Wrote {total_seq:,} sequences from {num_files} file{s} to directory "{out_dir}"')



# --------------------------------------------------
if __name__ == '__main__':
    main()

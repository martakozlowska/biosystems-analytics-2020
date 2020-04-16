#!/usr/bin/env python3
"""
Author : MK
Date   : 20.04.14
Purpose: Unclustered proteins
"""

import argparse
import os.path

import re
from Bio import SeqIO



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
                        required=True)
                        #default=None)

    parser.add_argument('-p',
                        '--proteins',
                        help='Proteins FASTA',
                        metavar='proteins',
                        type=argparse.FileType('r'),
                        required=True)
                        #default=None)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='outfile',
                        type=argparse.FileType('wt'),
                        default='unclustered.fa')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    clustered_ids = set()

    for line in args.cdhit:
        if line[0] != '>':
            match = re.search(r'>(\d+)', line)
            if match is not None:
                identities = match.group(1)
                clustered_ids.add(identities)
    n_seq = 0
    n_write = 0
    for rec in SeqIO.parse(args.proteins, 'fasta'):
        prot_id = re.sub(r'\|.*','', rec.id)
        n_seq += 1
        if prot_id not in clustered_ids:
            n_write += 1
            SeqIO.write(rec, args.outfile, 'fasta')

    print(f'Wrote {n_write:,} of {n_seq:,} unclustered proteins to "{args.outfile.name}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()

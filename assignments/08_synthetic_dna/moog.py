#!/usr/bin/env python3
"""
Author : MK
Date   : 20.03.31
Purpose: Moog time synthetic
"""

import argparse
import random
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Moog',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='file',
                        type=argparse.FileType('wt'),
                        default='out.fa')

    parser.add_argument('-t',
                        '--seqtype',
                        help='DNA or RNA',
                        metavar='str',
                        type=str,
                        choices=('dna', 'rna'),
                        default='dna')

    parser.add_argument('-n',
                        '--number',
                        help='Number of sequences to create',
                        metavar='int',
                        type=int,
                        default=10)

    parser.add_argument('-m',
                        '--minlen',
                        help='Minimum length',
                        metavar='int',
                        type=int,
                        default=50)

    parser.add_argument('-x',
                        '--maxlen',
                        help='Maximum length',
                        metavar='int',
                        type=int,
                        default=75)

    parser.add_argument('-p',
                        '--pctgc',
                        help='Percent GC',
                        metavar='float',
                        type=float,
                        default=0.5)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    args = parser.parse_args()

    if args.number < 1:
        parser.error(f'--number "{args.number}" must be > 0')

    if args.minlen < 1:
        parser.error(f'--minlen "{args.minlen}" must be > 0')

    if args.maxlen < 1:
        parser.error(f'--maxlen "{args.maxlen}" must be > 0')

    if not 0 < args.pctgc < 1:
        parser.error(f'--pctgc "{args.pctgc}" must be between 0 and 1')

    return args


# --------------------------------------------------
def create_pool(pctgc, max_len, seq_type):
    """ Create the pool of bases """

    t_or_u = 'T' if seq_type == 'dna' else 'U'
    num_gc = int((pctgc / 2) * max_len)
    num_at = int(((1 - pctgc) / 2) * max_len)
    pool = 'A' * num_at + 'C' * num_gc + 'G' * num_gc + t_or_u * num_at

    for _ in range(max_len - len(pool)):
        pool += random.choice(pool)

    return ''.join(sorted(pool))

def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    pool = create_pool(args.pctgc, args.maxlen, args.seqtype)

    for num in range(args.number):
        seq_len = random.randint(args.minlen, args.maxlen)
        seq = random.sample(pool, k=seq_len)
        args.outfile.write(f'> {num} \n{"".join(seq)}\n')

    end = 's' if args.number > 1 else ''
    file_name = os.path.basename(args.outfile.name)
    print(f'Done, wrote {args.number} {args.seqtype.upper()} sequence{end} to "{file_name}".')
    args.outfile.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()

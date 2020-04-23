#!/usr/bin/env python3
"""
Author : MK
Date   : 20.04.14
Purpose: Find TAIR locus ID
"""

import argparse
import re
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find TAIR locus ID',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        help='File to find TAIR gene IDs',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        nargs='+',
                        default=None,
                        required=True)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file name',
                        metavar='outfile',
                        type=argparse.FileType('wt'),
                        default='out.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    out_fh = args.outfile

    num_id, num_file, total_id = 0, 0, 0
    gil = []
    for fh in args.file:
        num_file += 1
        filename = os.path.basename(fh.name)
        print(f'{num_file:3}: {filename}')
        for line in fh:
            gene = re.search(r'AT(\d)G(\d+)', line)
            if gene is not None:
                gil.append(gene.group())

    sgil = set(gil)
    out_fh.write("\n".join(sgil)+'\n')

    num_id = len(sgil)

    s_num = '' if total_id is 1 else 's'
    s_file = '' if num_file is 1 else 's'
    print(f'Wrote {num_id} gene ID{s_num} from {num_file} file{s_file} to file "{args.outfile.name}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()

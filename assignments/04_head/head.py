#!/usr/bin/env python3
"""
Author : Marta Kozlowska
Date   : 02.25.2020
Purpose: Head
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Head',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='Number of lines (default: 10)',
                        type=int,
                        nargs='+',
                        default='10')

    parser.add_argument('file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default=[sys.stdin])

    return parser.parse_args()


# --------------------------------------------------
def main():
    """head time"""

    args = get_args()

    for fh in args.file:
        num_lines = 0
        for line in fh:
            num_lines += 1




# --------------------------------------------------
if __name__ == '__main__':
    main()

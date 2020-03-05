#!/usr/bin/env python3
"""
Author : MK
Date   : 20.03.03
Purpose: hamming time
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Hamming time',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default=None)

    parser.add_argument('-m',
                        '--min',
                        metavar=int,
                        default=0,
                        help='minimum integer value')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for line in args.file:
        line = line.strip()
        word1, word2 = line.split()

        if len(word1) == len(word2):
            diff = 0
            for c1, c2 in zip(word1, word2):
                if c1 == c2:
                    pass
                else:
                    diff += 1
        else: #words not the same length
            dist = 0
            diff = abs(len(word1) - len(word2))
            for c1, c2 in zip(word1, word2):
                if c1 == c2:
                    pass
                else:
                    dist += 1
                diff += dist

        if args.min >= 0:

            print(f'{diff:8}:{word1:20}{word2}')

# --------------------------------------------------
if __name__ == '__main__':
    main()

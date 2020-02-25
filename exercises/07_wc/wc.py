#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Toilet? wc',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='*',
                        type=argparse.FileType('r'),
                        default=[sys.stdin],
                        help='input file(s)')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """toilet time"""

    args = get_args()
    total_lines = 0
    total_words = 0
    total_chars = 0

    for fh in args.file:
        num_lines = 0
        num_words = 0
        num_chars = 0
        for line in fh:
            num_lines += 1
            words = line.split()
            num_words += len(words)
            num_chars += len(line)

        total_lines += num_lines
        total_words += num_words
        total_chars += num_chars

        print(f'{num_lines:8}{num_words:8}{num_chars:8} {fh.name}')

    if len(args.file) > 1:
        print(f'{total_lines:8}{total_words:8}{total_chars:8} total')

# --------------------------------------------------
if __name__ == '__main__':
    main()

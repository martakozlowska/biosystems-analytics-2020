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

    parser.add_argument('file',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default=None)
    parser.add_argument('-n',
                        '--num',
                        help='Number of lines to show',
                        type=int,
                        default='10')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """head time"""

    args = get_args()

    for fh in args.file:




# --------------------------------------------------
if __name__ == '__main__':
    main()

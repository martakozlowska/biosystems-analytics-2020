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
                        default='10')

    parser.add_argument('file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default=[sys.stdin])

    args = parser.parse_args()
    if not args.num > 0:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args


# --------------------------------------------------
def main():
    """head time"""

    args = get_args()

    fh = open(args.file)
    text = fh.readline(args.num)
    print(text)



    #for fh in args.file:
        #num_lines = 0
        #for line in fh:
            #num_lines += 1




# --------------------------------------------------
if __name__ == '__main__':
    main()

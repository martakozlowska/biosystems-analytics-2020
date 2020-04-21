#!/usr/bin/env python3
"""
Author : MK
Date   : 20.04.14
Purpose: Find TAIR locus ID
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find TAIR locus ID',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-t',
                        '--tair',
                        help='File to find TAIR accession number',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        nargs='+',
                        default=None,
                        required=True)

    parser.add_argument('-o',
                        '--output',
                        help='Output file name',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default='out.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()



# --------------------------------------------------
if __name__ == '__main__':
    main()

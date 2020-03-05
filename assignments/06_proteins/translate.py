#!/usr/bin/env python3
"""
Author : Marta Kozlowska
Date   : 20.03.05
Purpose: Protein translate
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Protein translate time',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('DNA',
                        metavar='str',
                        type=str,
                        help='DNA/RNA sequence')

    parser.add_argument('-c',
                        '--codons',
                        help='A file with codon translations',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default=None)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        type=str,
                        default='out.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Protein time"""

    args = get_args()

    print(args.DNA)


# --------------------------------------------------
if __name__ == '__main__':
    main()

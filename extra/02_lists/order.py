#!/usr/bin/env python3
"""
Author : Marta Kozlowska
Date   : 2020.02.11
Purpose: Order stuff
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Order stuff',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('words',
                        metavar='str',
                        nargs='*',
                        help='Input words to order')
    parser.add_argument('-r',
                        '--reverse',
                        help='Reverse order',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Order stuff"""

    args = get_args()
    words = args.words
    alphabet = words.sort()
    ind = '\nindex'

    print(f'{ind.join(alphabet)}')

# --------------------------------------------------
if __name__ == '__main__':
    main()

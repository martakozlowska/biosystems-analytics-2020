#!/usr/bin/env python3
"""
Author : Marta Kozlowska
Date   : 2020.02.27
Purpose: Gashlycrumb
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Crumb',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letters',
                        metavar='str',
                        nargs='+'
                        help='Letters to lookup')

    parser.add_argument('-f',
                        '--file',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default='gashlycrumb.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    print(f'letters = {args.letters}')
    print(f'text = {}')


# --------------------------------------------------
if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
Author : MK
Date   : 02.06.2020
Purpose: DNA time
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='How many bases',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('DNA',
                        metavar='str',
                        help='DNA sequence')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    DNA = args.DNA

    if DNA.islower():
        print(f'{DNA.count("a")} {DNA.count("c")} {DNA.count("g")} {DNA.count("t")}')
    else:
        print(f'{DNA.count("A")} {DNA.count("C")} {DNA.count("G")} {DNA.count("T")}')

# --------------------------------------------------
if __name__ == '__main__':
    main()

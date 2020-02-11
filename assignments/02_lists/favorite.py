#!/usr/bin/env python3
"""
Author : Marta Kozlowska
Date   : 02.06.2020
Purpose: My Favourite Things
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='What are my favourite things',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('things',
                        metavar='str',
                        nargs='+',
                        help='Favourite things')

    parser.add_argument('-s',
                        '--sep',
                        default=', ',
                        help='A separator')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """list favorite things"""

    args = get_args()
    things = args.things
    sep = args.sep

    if sep: print(f'{sep.join(things)}')

    if len(things) == 1:
        print(f'This is one of my favorite things.')
    else:
        print(f'These are a few of my favorite things.')

# --------------------------------------------------
if __name__ == '__main__':
    main()

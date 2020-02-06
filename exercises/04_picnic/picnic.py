#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Picnic time !!
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic time !!',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items',
                        metavar='str',
                        nargs='+',
                        help='bringing to picnic')
    parser.add_argument('-s',
                        '--sorted',
                        action='store_true',
                        help='sort the items')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """bringing to picnic"""

    args = get_args()
    items = args.items

    if args.sorted: items.sort()

    if len(items) == 1:
        print(f'You are bringing {items[0]}.')
    elif len(items) == 2:
        print(f'You are bringing {" and ".join(items)}.')
    else:
        print(f'You are bringing {", ".join(items[:-2])}, {items[-2]}, and {items[-1]}.')

# --------------------------------------------------
if __name__ == '__main__':
    main()

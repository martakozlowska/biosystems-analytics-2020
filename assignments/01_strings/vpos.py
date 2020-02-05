#!/usr/bin/env python3
"""
Author : Marta Kozlowska
Date   : 01.28.2020
Purpose: What's in the water
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Crows nest',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('water',
                        metavar='str',
                        help='in the water')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """What's in the water"""

    args = get_args()
    water = args.water
    article = 'an' if water[0].lower() in 'aeiou' else 'a'

    print(f'Ahoy, Captain, {article} {water} off the larboard bow!')

# --------------------------------------------------
if __name__ == '__main__':
    main()

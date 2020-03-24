#!/usr/bin/env python3
"""
Author : MK
Date   : 20.03.23
Purpose: Apples & Bananas
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel to substitute',
                        metavar='str',
                        type=str,
                        default='a',
                        choices=list('aeiou'))

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    vowel = args.vowel

    new_text = []
    for char in text:
        if char in 'aeiou':
            new_text.append(vowel)
        elif char in 'AEIOU':
            new_text.append(vowel.upper())
        else:
            new_text.append(char)

    print(''.join(new_text))



# --------------------------------------------------
if __name__ == '__main__':
    main()

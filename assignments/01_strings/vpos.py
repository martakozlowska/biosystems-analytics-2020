#!/usr/bin/env python3
"""
Author : Marta Kozlowska
Date   : 02.04.2020
Purpose: Vowels
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find position of a vowel in string',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('vowel',
                        metavar='str',
                        help='a vowel to look for',
                        choices=['a','e','i','o','u','A','E','I','O','U'])
    parser.add_argument('text',
                        metavar='str',
                        help='The text to search')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Find position of vowel in string"""

    args = get_args()
    vowel = args.vowel
    text = args.text

    if vowel in text:
        print(f'Found "{vowel}" in "{text}" at index {text.index(vowel)}.')
    else:
        print(f'"{vowel}" is not found in "{text}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()

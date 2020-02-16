#!/usr/bin/env python3
"""
Author : Marta Kozlowska
Date   : 02.13.2020
Purpose: Jump the 5
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the 5',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Jump to 5"""

    args = get_args()
    text = args.text
    numbers = {'0': '5', '1': '9', '2': '8', '3': '7', '4': '6', '5': '0', '6': '4', '7': '3', '8': '2', '9': '1'}

    for char in text:
        #print(char, char in numbers)
        #if char in numbers:
        #    print(numbers[char])
        #else:
        #    print(char)

        #print(numbers[char] if char in numbers else char, end = '')

        print(numbers.get(char, char), end='')
    print()

# --------------------------------------------------
if __name__ == '__main__':
    main()

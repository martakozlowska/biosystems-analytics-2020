#!/usr/bin/env python3
"""
Author : Marta Kozlowska
Date   : 02.25.2020
Purpose: Head
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Head',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input file',
                        metavar='FILE')

    parser.add_argument('-n',
                        '--num',
                        help='Number of lines (default: 10)',
                        type=int,
                        default=10)



    args = parser.parse_args()
    if not args.num > 0:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args


# --------------------------------------------------
def main():
    """head"""

    args = get_args()

    #fh = open(arg.file)
        #count = 0
        #num_lines = range (0, args.num)
        #for line in fh:
            #line = line.strip()
            #if count in num_lines:
                #print(line)
            #else:
                #pass


    #N = args.num
    #for i in range(N):
        #line = args.file.strip()
        #print(line)

    with open(args.file) as fh:
        num_lines = 0

        for line in fh:
            line = line.strip()
            if num_lines in range (0, args.num):
                print(line)
            num_lines += 1

    #if int(num_lines) < int(args.num):
        #print(fh.readline())


# --------------------------------------------------
if __name__ == '__main__':
    main()

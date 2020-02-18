#!/usr/bin/env python3
"""
Author : Marta Kozlowska
Date   : 02.18.2020
Purpose: Howler
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text or file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file name',
                        metavar='str',
                        type=str,
                        default='')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args

# --------------------------------------------------
def main():
    """Howler time"""

    args = get_args()
    out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout
    #out_fh.write(args.text.upper() + '\n')
    print(args.text.upper(), file=out_fh, end='')
    print('OHNOES', file=sys.stderr)
    out_fh.close()

# --------------------------------------------------
if __name__ == '__main__':
    main()

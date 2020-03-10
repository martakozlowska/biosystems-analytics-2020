#!/usr/bin/env python3
"""
Author : Marta Kozlowska
Date   : 20.03.05
Purpose: Protein translate
"""

import argparse
import os
import sys
from pprint import pprint


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Protein translate time',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('DNA',
                        metavar='str',
                        type=str,
                        help='DNA/RNA sequence')

    parser.add_argument('-c',
                        '--codons',
                        help='A file with codon translations',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default=None)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        type=str,
                        default='out.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Protein time"""

    args = get_args()

    lookup = {line[:3]: line.strip()[4:] for line in args.codons}
    #pprint(lookup)

    seq = args.DNA.upper()
    seq_code = [seq[i:i+3] for i in range(0, len(seq), 3)]
    #print(seq_code)

    for cdn in seq_code:
        ans = lookup.get(cdn, f'-')
    return ans
    print(ans)

    out_fh = open(args.outfile, 'w')
    out_fh.write(ans)

"""
print(lookup.get(letter.upper(), f'I do not know "{letter}".'))
    for codon in args.DNA:
        print(lookup.get(codon[:2], f'-'), end='')

    out_fh = open(args.outfile, 'wt') #if args.outfile else sys.stdout


    print(args.text.upper(), file=out_fh, end='')
    print('OHNOES', file=sys.stderr)
    out_fh.close()

    print(f'Output written to {out_fh}')
"""

# --------------------------------------------------
if __name__ == '__main__':
    main()

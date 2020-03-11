#!/usr/bin/env python3
"""
Author : Marta Kozlowska
Date   : 20.03.05
Purpose: Protein translate
"""

import argparse


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
                        default=None,
                        required=True)

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

    #seq = args.DNA.upper()
    seq_code = [args.DNA.upper()[i:i+3] for i in range(0, len(args.DNA), 3)]

    ans = ''
    for cdn in seq_code:
        ans += lookup.get(cdn, f'-')

    out_fh = open(args.outfile, 'wt')
    out_fh.write(ans + '\n')
    print(f'Output written to "{args.outfile}".')
    out_fh.close()

# --------------------------------------------------
if __name__ == '__main__':
    main()

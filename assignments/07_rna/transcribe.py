#!/usr/bin/env python3
"""
Author : Marta Kozlowska
Date   : 20.03.23
Purpose: DNA RNA transcribe
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Transcription time',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input file(s)',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default=None,
                        nargs='+')

    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory',
                        type=str,
                        default='out')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Transcription time"""

    args = get_args()
    outdir = args.outdir

    if not os.path.isdir(outdir):
        os.makedirs(outdir)

    num_seq = 0
    num_file = 0
    numseq_total = 0
    for fh in args.file:
        out_file = os.path.join(outdir, os.path.basename(fh.name))
        out_fh = open(out_file, 'wt')
        num_file += 1
        RNA = []
        for line in fh:
            num_seq += 1
            for char in line:
                if char is 't':
                    RNA.append('u')
                elif char is 'T':
                    RNA.append('U')
                else:
                    RNA.append(char)

        numseq_total += num_seq
        seq_s = 'sequence' if num_seq == 1 else 'sequences'
        file_s = 'file' if num_file == 1 else 'files'
        out_fh.write(''.join(RNA))
        print(f'Done, wrote {numseq_total} {seq_s} in {num_file} {file_s} to directory "{outdir}".')
        out_fh.close()

# --------------------------------------------------
if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""tests for accession.py"""

import os
import random
import re
import string
from subprocess import getstatusoutput
from Bio import SeqIO
from Bio.SeqUtils import GC
from numpy import mean
from itertools import chain
from shutil import rmtree

prg = './accession.py'
amigo = './amigo_heat.txt'
tair = './tair_heat.txt'
outfile = 'atg.txt'

# --------------------------------------------------
def test_exists():
    """usage"""

    for file in [prg, amigo, tair]:
        assert os.path.isfile(file)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput('{} {}'.format(prg, flag))
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)

# --------------------------------------------------
def test_missing_file():
    """fails on no input"""

    rv, out = getstatusoutput(f'{prg} -o {outfile}')
    assert rv != 0
    assert re.search('the following arguments are required: -t/--tair',
                     out)

# --------------------------------------------------
def test_bad_file():
    """die on bad file"""

    bad = random_string()
    rv, out = getstatusoutput(f'{prg} -t {bad}')
    assert rv != 0
    assert re.match('usage:', out, re.I)
    assert re.search(f"No such file or directory: '{bad}'", out)

# --------------------------------------------------
def test_amigo():
    """runs on AmiGO file"""

    out_file = 'out.txt'
    try:
        if os.path.isfile(out_file):
            os.remove(out_file)

        rv, out = getstatusoutput(f'{prg} -t {amigo}')
        assert rv == 0
        expected = ('  1: amigo_heat.txt\n'
                    'Wrote 16 accession IDs from 1 file to file "out.txt"')
        assert out == expected
        assert os.path.isfile(out_file)

        # correct number of seqs
        seqs = out_file.readlines()
        assert len(seqs) == 16

        # the lengths are in the correct range
        seq_lens = list(map(lambda seq: len(seq.seq), seqs))
        assert max(seq_lens) <= 75
        assert min(seq_lens) >= 50

        # bases are correct
        bases = ''.join(
            sorted(
                set(chain(map(lambda seq: ''.join(sorted(set(seq.seq))),
                              seqs)))))
        assert bases == 'ACGT'

        # the pct GC is about right
        gc = list(map(lambda seq: GC(seq.seq) / 100, seqs))
        assert .47 <= mean(gc) <= .53

    finally:
        if os.path.isfile(out_file):
            os.remove(out_file)


# --------------------------------------------------
def test_options():
    """runs on good input"""

    out_dir = random_string()
    try:
        if os.path.isdir(out_dir):
            rmtree(out_dir)

        cmd = f'{prg} -s 4 -o {out_dir} -p .25 {n1k} {n10k} {n100k}'
        print(cmd)
        rv, out = getstatusoutput(cmd)
        assert rv == 0

        assert re.search('1: n1k.fa', out)
        assert re.search('2: n10k.fa', out)
        assert re.search('3: n100k.fa', out)
        assert re.search(
            f'Wrote 27,688 sequences from 3 files to directory "{out_dir}"',
            out)

        assert os.path.isdir(out_dir)

        files = os.listdir(out_dir)
        assert len(files) == 3

        seqs_written = 0
        for file in files:
            seqs_written += len(
                list(SeqIO.parse(os.path.join(out_dir, file), 'fasta')))

        assert seqs_written == 27688
    finally:
        if os.path.isdir(out_dir):
            rmtree(out_dir)

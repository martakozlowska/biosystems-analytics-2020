#!/usr/bin/env python3
"""tests for gene_ids.py"""

import os
import random
import re
import string
from subprocess import getstatusoutput

prg = './gene_ids.py'
amigo = './inputs/amigo_heat.txt'
tair = './inputs/tair_heat.txt'
repeat = './inputs/amigo_repeat'
outfile = 'out.txt'
#exp_amigo = "\n".join(('AT5G12020 AT5G41340 AT5G03720 AT4G14690 AT2G22360 AT2G33590 AT1G54050 AT3G10800 AT3G04120 AT1G64280 AT5G12140 AT3G24520 AT3G24500 AT4G19630 AT3G06400 AT1G16030').split())
exp_tair = "\n".join(('AT5G67030 AT1G13930 AT3G09440 AT1G16540 AT2G22360').split())
exp_two = "\n".join(('AT5G67030 AT1G13930 AT3G09440 AT1G16540 AT2G22360 AT5G12020 AT5G41340 AT5G03720 AT4G14690 AT2G22360 AT2G33590 AT1G54050 AT3G10800 AT3G04120 AT1G64280 AT5G12140 AT3G24520 AT3G24500 AT4G19630 AT3G06400 AT1G16030').split())
exp_repeat = "\n".join(('AT5G12020 AT5G41340 AT5G03720 AT4G14690 AT2G22360').split())

exp_amigo = 'AT5G12140 AT1G16030 AT4G19630\nAT2G22360\nAT5G03720\nAT2G33590\nAT1G54050\nAT3G04120\nAT1G64280\nAT3G10800\nAT3G06400\nAT4G14690\nAT3G24520\nAT5G41340\nAT5G12020\nAT3G24500'

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
    assert re.search('the following arguments are required: -f/--file',
                     out)

# --------------------------------------------------
def test_bad_file():
    """die on bad file"""

    bad = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    rv, out = getstatusoutput(f'{prg} -f {bad}')
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

        rv, out = getstatusoutput(f'{prg} -f {amigo}')
        assert rv == 0
        expected = ('  1: amigo_heat.txt\n'
                    'Wrote 16 gene IDs from 1 file to file "out.txt"')
        assert out == expected
        assert os.path.isfile(out_file)

        # correct number of seqs
        #seqs = out_file.readlines()
        #assert len(seqs) == 16

        # correct gene names
        #assert out_file == exp_amigo

    finally:
        if os.path.isfile(out_file):
            os.remove(out_file)


# --------------------------------------------------
def test_tair():
    """runs on TAIR file"""

    out_file = 'out.txt'
    try:
        if os.path.isfile(out_file):
            os.remove(out_file)

        rv, out = getstatusoutput(f'{prg} -f {tair}')
        assert rv == 0
        expected = ('  1: tair_heat.txt\n'
                    'Wrote 5 gene IDs from 1 file to file "out.txt"')
        assert out == expected
        assert os.path.isfile(out_file)

        # correct number of seqs
        #seqs = out_file.readlines()
        #assert len(seqs) == 5

        # correct gene names
        #assert out_file == exp_tair

    finally:
        if os.path.isfile(out_file):
            os.remove(out_file)

# --------------------------------------------------
def test_two_files():
    """runs on TAIR and AmiGO file"""

    out_file = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    try:
        if os.path.isfile(out_file):
            os.remove(out_file)

        rv, out = getstatusoutput(f'{prg} -f {tair} {amigo} -o {out_file}')
        assert rv == 0
        assert re.search('1: tair_heat.txt', out)
        assert re.search('2: amigo_heat.txt', out)
        assert re.search(
            f'Wrote 20 gene IDs from 2 files to file "{out_file}"',
            out)
        assert os.path.isfile(out_file)

        # correct number of seqs
        #seqs = out_file.readlines()
        #assert len(seqs) == 20

        # correct gene names
        #assert out_file == exp_two

    finally:
        if os.path.isfile(out_file):
            os.remove(out_file)

# --------------------------------------------------
def test_repeat_seq():
    """runs on AmiGO file with repeated sequences"""

    out_file = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    try:
        if os.path.isfile(out_file):
            os.remove(out_file)

        rv, out = getstatusoutput(f'{prg} -f {repeat} -o {out_file}')
        #assert rv == 0
        # assert re.search('1: amigo_repeat.txt', out)
        # assert re.search(
        #     f'Wrote 5 gene IDs from 1 file to file "{out_file}"',
        #     out)
        # assert os.path.isfile(out_file)

        # correct number of seqs
        #seqs = out_file.readlines()
        #assert len(seqs) == 5

        # correct gene names
        #assert out_file == exp_repeat

    finally:
        if os.path.isfile(out_file):
            os.remove(out_file)
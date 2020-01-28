#!/usr/bin/env python3
"""
Author : Marta Kozlowska <mkozlowska@email.arizona.edu>
Date   : 27.01.2020
Purpose: Crow's Nest exercise
"""

import argparse
import os
import re
import subprocess
import sys
from datetime import date
from pathlib import Path


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='CrowsNest',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("water",
                        help="what's in the water",
                        metavar="str",
                        type=str,
                        default="")
    if water[0].lower() in 'aeiou'
        article = 'an'
    else:
        article = 'a'
    return parser.parse_args()


# --------------------------------------------------
def main():
    """What's in the water?"""
    args=get_args()
    print("Ahoy, Captain, {} {} off the larboard bow!".format(article,water))


# --------------------------------------------------
if __name__ == '__main__':
    main()

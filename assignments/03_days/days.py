#!/usr/bin/env python3
"""
Author : Marta Kozlowska
Date   : 02.16.2020
Purpose: Days of the Week
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Days of the week',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('days',
                        metavar='str',
                        nargs='+',
                        help='Days of the Week')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """What you do on days of the week"""

    args = get_args()
    days = args.days
    week = {
        "Monday": "On Mondays I never go to work",
        "Tuesday": "On Tuesdays I stay at home",
        "Wednesday": "On Wednesdays I never feel inclined",
        "Thursday": "On Thursdays, it's a holiday",
        "Friday": "And Fridays I detest",
        "Saturday": "Oh, it's much too late on a Saturday",
        "Sunday": "And Sunday is the day of rest"
        }

    for days in args.days:
        print(week.get(days) if days in week else f'Can\'t find "{days}"')

# --------------------------------------------------
if __name__ == '__main__':
    main()

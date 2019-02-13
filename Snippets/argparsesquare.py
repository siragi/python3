#!/usr/bin/python3
# https://docs.python.org/2/howto/argparse.html

import argparse
parser = argparse.ArgumentParser()
parser.add_argument(
    "square", help="Display a square of a given number", type=int)
args = parser.parse_args()
print(args.square**2)

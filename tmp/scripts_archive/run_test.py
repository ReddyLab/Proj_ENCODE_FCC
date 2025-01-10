###
import numpy  as np
import pandas as pd
print("Run test Python script")

###
import argparse
parser = argparse.ArgumentParser()
parser.add_argument(
    "echo", 
    help = "echo the string you use here",
    type = str
)

parser.add_argument(
    "-v", "--verbose", 
    help   = "increase output verbosity",
    action = "store_true"
)

###
args = parser.parse_args()
txt  = args.echo

if args.verbose:
    print("Verbosity turned on")

if args.verbose:
    print(txt)


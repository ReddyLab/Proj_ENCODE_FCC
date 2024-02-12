
import argparse
import os

def parse_args():
    """Parse arguments from command line"""
    
    ### set arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--fout', help='foo help')
    parser.add_argument('--verbose',  action='store_true', help='foo help')
    
    ### parse arguments and return
    args=parser.parse_args()
    return args
    
def main(fout = None, verbose = False):
    paths = os.listdir(fout)
    for path in paths:
        print(path)
    
if __name__ == "__main__":
    args = parse_args()
    main(**vars(args))
    

#! /usr/bin/python
import argparse
import sys
from sourcefile import sourcefile
from plotsamples import plotsamples

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='rds control options')
    parser.add_argument('-f', dest='filename',help="file name with the sampled data")
    parsed_args=parser.parse_args(sys.argv[1:])
    if parsed_args.filename is None:
        sys.exit(1)
    src=sourcefile(parsed_args.filename)
    pltsamp=plotsamples(src)
    src.read_samples()
    print src.get_samples_types()
    print src.get_sampling_rate()
    print src.get_osc_freq()

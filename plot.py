#!/usr/bin/env python
import matplotlib.pyplot as pl
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', default='data.dat', type=str)
parser.add_argument('-o', default='plot-data.png', type=str)
args = parser.parse_args()

def plot_data(data_path=None):
    fig, ax = pl.subplots()
    data = np.loadtxt(data_path)
    ax.plot(data[:,0], data[:,1])
    return fig

if __name__=='__main__':
    fig = plot_data(args.i)
    fig.savefig(args.o)

#!/usr/bin/env python
from matplotlib.figure import Figure
import sys
sys.path.append("..")
from plot import plot_data

def test_plot():
    fig = plot_data('../data.dat')
    assert isinstance(fig, Figure)

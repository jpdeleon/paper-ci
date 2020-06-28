#!/usr/bin/env python
from matplotlib.figure import Figure
import sys
sys.path.append("./figures")
import plot

def test_plot():
    fig = plot.plot_data('./figures/data.dat')
    assert isinstance(fig, Figure)

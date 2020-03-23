# -*- coding: utf-8 -*-
# -*- mode: python -*-
"""Functions for file IO"""
import pandas as pd

data = pd.read_csv('../data/crcns/aa2/stim_data.csv', header=None)
#print(data)
#print(data[data.columns[0]])

def read_spike(id, data):
    # """Describe what the arguments of the function mean and what the function returns"""
    # where data[data.columns[0]]) == id
    print(data.loc[data[data.columns[0]] == id])


#read_spike('1383E39141408603333A806AF75B4132.wav',data)





#from __future__ import print_function, division, absolute_import


#input ID# to return columns: sample rate, depth, number of samples, and class of stimulus

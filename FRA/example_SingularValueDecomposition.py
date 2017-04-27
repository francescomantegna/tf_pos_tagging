#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 14:16:59 2017

@author: patrizio
"""

from numpy import *
import operator
from os import listdir
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from numpy.linalg import *
from scipy.stats.stats import pearsonr
from numpy import linalg as la
 
# load data points
raw_data = loadtxt('iris_proc.data',delimiter=',',skiprows=1)
samples,features = shape(raw_data)
 
#normalize and remove mean
data = mat(raw_data[:,:4])
 
def svd(data, S=2):
     
    #calculate SVD
    U, s, V = linalg.svd( data )
    Sig = mat(eye(S)*s[:S])
    #tak out columns you don't need
    newdata = U[:,:S]
     
    # this line is used to retrieve dataset 
    #~ new = U[:,:2]*Sig*V[:2,:]
 
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    colors = ['blue','red','black']
    for i in xrange(samples):
        ax.scatter(newdata[i,0],newdata[i,1], color= colors[int(raw_data[i,-1])])
    plt.xlabel('SVD1')
    plt.ylabel('SVD2')
    plt.show()
         
 
svd(data,2)
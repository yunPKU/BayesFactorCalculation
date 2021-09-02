#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 10:56:12 2021

@author: macbjmu
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
0419
adopt for more than three XFD sequences
@author: macbjmu
"""
import csv
import pandas as pd
import numpy as np
from sklearn.neighbors import KernelDensity
from scipy.stats import norm
import os 






def skip_to(fle,**kwargs):
  if os.stat(fle).st_size == 0:
    raise ValueError("File is empty")
  with open(fle) as f:
    pos = 0
    cur_line = f.readline()
    while not cur_line.find('Sample')>=0:
        pos = f.tell()
        cur_line = f.readline()
    f.seek(pos)
    return pd.read_csv(f, **kwargs)



def BayesFactorCal(logPath,fileIN,span,vlinePos):
    logdata = skip_to(logPath+fileIN, sep='\t', header=0);
    
    '''
    2 estimate the posterior for the interested variable
    '''
    XfdNum = len(vlinePos)
    label_bj = []
    label_CT = []
    label_plt = []
    smpDate = []
    for label in logdata.columns.values:
        if 'CT|' in label:  label_CT.append(label)
        if 'BK|' in label:  
            label_bj.append(label)
            label_plt.append('Beijing/'+label.split('/')[1]+'/2020')
    label_plt.append('Control Sequence')
    label_bj = label_bj + label_CT
    label_bj_short = []
    cont = 0
    for label in label_bj:
        if cont < XfdNum:     
            label_bj_short.append((label.split('|')[1]))
        else:
            label_bj_short.append(label.split('|')[1])
        cont += 1 
    
    brn_in = 0.1 # the ratio of burn-in
    
    
    seqNum = len(label_bj_short)
    # seqNum = 3
    BF_total = pd.DataFrame(label_bj_short)
    BF_total.columns = ['tip']
    BFre = np.zeros(seqNum)
    gridNum  = 100
    X_plot = np.linspace(2020, 2021, gridNum).reshape(-1,1)
    
    
    cnst_BD = 0.01
    
    '''
    calculation of BF
    '''
    for i in range(seqNum):
        templabel = label_plt[i] if i<len(label_plt) else label_plt[-1]
        varb = logdata[label_bj[i]].values.reshape(-1,1)
        tempSt = int(varb.size*brn_in);
        data = np.hstack((data,varb[tempSt:-1])) if i >0 else varb[tempSt:-1]
    
    
    for i in range(seqNum):    
        kde = KernelDensity(kernel='gaussian', bandwidth=cnst_BD).fit(data[:,i].reshape(-1,1))
        BFre[i] = (np.exp(kde.score_samples([[vlinePos[i]]]))[0]*span)**(-1) 
    return BFre;


logPath = '/Users/macbjmu/'
fileIN  = 'B11_29_gis_big_smpSize=10_before1130_iter=6.log' 
span    = 0.9151
vlinePos = [2020.4411,2020.4438,2020.4438,2020.4466,2020.4466,2020.4521,2020.463] + [2020.4438]*5

BF = BayesFactorCal(logPath,fileIN,span,vlinePos);


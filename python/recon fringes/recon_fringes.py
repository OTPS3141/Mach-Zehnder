# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 14:20:15 2021

@author: OTPS
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from read_bin import read_data



data_list = []

for i in range(1, 10):
    
    data_list.append(f"20211119-000{i}.csv")
    
for i in range(10, 21):
    
    data_list.append(f"20211119-00{i}.csv")
    
        
t_list = []
A_list = []
B_list = []

for i in range(0, 20):
    
    t, A, B = read_data(data_list[i])
    
    t_list.append(t)
    A_list.append(A)
    B_list.append(B)

start = 0 
end = t_list[0].size

# for i in range(0,20):
    
    

#     plt.figure()
#     plt.plot(t_list[i][start:end], A_list[i][start:end] ,'-', label = "PM signal")
#     plt.legend(loc="best")
    
#     plt.plot(t_list[i][start:end], B_list[i][start:end] ,'-', label = "Piezo ramp", color = 'red')
#     plt.legend(loc="best")
#     plt.title(f"Data 20211119-000{i+1} ")
#     plt.show()
    
    
### Merge A over start - end

merge_A = np.zeros(end)

for i, A in enumerate(A_list):
    
    for j in range(0, end):
        
        merge_A[j] += A[j]
        
    
### Averaging

merge_A = merge_A / 20
        
        
plt.figure()
plt.plot(t_list[0][start:end], merge_A ,'-', label = "PM signal")
plt.plot(t_list[0][start:end], B_list[0][start:end] ,'-', label = "Piezo ramp", color = 'red')
plt.legend(loc="best")
plt.show()


    



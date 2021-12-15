# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 17:10:25 2021

@author: OTPS
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

### Time (s), Channel A (V), Channel B (mV)

class read:
    def __init__(self, data) -> None:
        self.data = data
       

    def read_data(self):

        self.df = pd.read_csv(self.data, delimiter=',', names = ['time', 'channel_A', 'channel_B'], low_memory=False, usecols=["time", "channel_B"]) 
        self.df = self.df.drop([0,1,2], axis=0)
        
        self.time = np.array(self.df.time).astype(np.float)
        self.B = np.array(self.df.channel_B).astype(np.float)
        
        return self.time, self.B

    
# df_noclass = pd.read_csv("Data\Photon statistics\statistics\pm_pos1_1\pm_pos1_1_1.csv", delimiter=',', names = ['time', 'channel_A', 'channel_B'], low_memory=False, usecols=["time", "channel_B"]) 
df = read("Data\Photon statistics\statistics\pm_pos1_1\pm_pos1_1_1.csv")
time, B = df.read_data()



def plot(time, B):



    plt.figure()
    plt.plot(time, B,'-', label = "PM Signal", color = 'red')
    plt.legend(loc="best")
    plt.xlabel("Time [s]")
    plt.ylabel("Voltage [mV]")
    plt.show()


plot(time, B)

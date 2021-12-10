import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


'''
Read oscilloscope
'''




PD_data = pd.read_csv("Data\Wave nature - oscilloscope\F0016CH1.csv", delimiter=',', usecols=[3,4], names=['time', 'channel'])
PZT_data = pd.read_csv("Data\Wave nature - oscilloscope\F0016CH2.csv", delimiter=',', usecols=[3,4], names=['time', 'channel'])


t = np.array(PD_data.time).astype(np.float)
A = np.array(PD_data.channel).astype(np.float)
B = np.array(PZT_data.channel).astype(np.float)


fig,ax = plt.subplots()
ax.plot(t, A)
ax.set_xlabel("Time [s]")
ax.set_ylabel("Voltage [V]")
ax2 = ax.twinx()

ax2.plot(t, B, color='red')
ax.set_xlabel("Time [s]")
ax.set_ylabel("Voltage [V]")
plt.show()

""" plt.figure()
plt.plot(t, A)
plt.figure()
plt.plot(t, B)
plt.show() """

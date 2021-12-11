import numpy as np
import matplotlib.pyplot as plt

from matplotlib import rc
rc('text', usetex=True) # Use LaTeX font

import seaborn as sns
sns.set(color_codes=True)

import scipy as scipy
from scipy import optimize

'''
Quantum eraser data analysis
'''


### Plot theory 

fig, ax = plt.subplots(1)
x = np.linspace(0, 0.5 * np.pi, 1001)
y = np.abs(np.cos(2*x))
ax.plot(x, y)
plt.xlim(0, 0.5 * np.pi)

ax.set_xticks(np.arange(0, 0.5 * np.pi+0.01, np.pi/4))
labels = ['$0$', r'$\pi/4$', r'$\pi/2$']
ax.set_xticklabels(labels)


### Observations QE

# theta_eraser = np.arange(0, 95, 5)

fig2, ax2 = plt.subplots(1)
x2 = np.linspace(0, 0.5 * np.pi, 19)
contrast_eraser = np.array([0.35, 0.365, 0.36, 0.308, 0.307, 0.302, 0.234, 0.181, 0.131, 0.078, 0.038, 0.062, 0.116, 0.169, 0.225, 0.268, 0.288, 0.365, 0.348])
ax2.plot(x2, contrast_eraser)
plt.xlim(0, 0.5 * np.pi)

ax2.set_xticks(np.arange(0, 0.5 * np.pi+0.01, np.pi/4))
labels = ['$0$', r'$\pi/4$', r'$\pi/2$']
ax2.set_xticklabels(labels)

# plt.show()

### Fit data to cos(2x)

def func(x, a, b, c):

    return a + np.abs(np.cos(2 * b * x)) * c

def fit(func, x, y, a, b, c):

    popt, pcov = scipy.optimize.curve_fit(func, x, y, p0=[a, b, c])
    
    print("Parameters: ",popt)
    
    popt = np.round(popt, 4)
    perr = np.round(np.sqrt(np.diag(pcov)), 4)
    print("Errors: ", perr)

    print(f"$({popt[0]} \pm {perr[0]})$ & $({popt[1]} \pm {perr[1]})$ & $({popt[2]} \pm {perr[2]})$")
    
    fig3, ax3 = plt.subplots(1)

    ax3.plot(x, y, '-o', color='lightgrey', label = 'Observed contrast')  
    ax3.set_xlabel('Angle [rad]')
    ax3.set_ylabel('Contrast [a.u.]') 
    ax3.set_title('Fit of $a + c|cos(2bx)|$ to observed contrast')
    ax3.grid(True)
    ax3.plot(x, func(x, popt[0], popt[1], popt[2], ), 'red', label='Fitting function $a + c|cos(2bx)|$')
    ax3.legend(loc = "best")

    plt.xlim(0, 0.5 * np.pi)

    ax3.set_xticks(np.arange(0, 0.5 * np.pi+0.01, np.pi/4))
    labels = ['$0$', r'$\pi/4$', r'$\pi/2$']
    ax3.set_xticklabels(labels)

    # plt.plot(x, y, '-o', color='lightgrey', label = 'Data')
    # plt.title('Fit')
    # plt.xlabel('Angle [rad]')
    # plt.ylabel('Contrast [a.u.]')
    # plt.grid(True)
    # plt.plot(x, func(x, popt[0], popt[1], popt[2], ), 'red', label='Fit')
    # plt.legend(loc='best')

    plt.show()

fit(func, x2, contrast_eraser, 1, 1, 1)


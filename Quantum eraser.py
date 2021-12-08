import numpy as np
import matplotlib.pyplot as plt

'''
Quantum eraser data analysis
'''

### Plot theory 

x = np.linspace(0, np.pi, 100)

def cos(x):
    
    
    return np.abs(np.cos(2*x))


plt.figure()

plt.plot(x, cos(x))

plt.show()

### Eraser x = -45, P1 x = 45

theta_eraser = np.arange(0, 95, 5)

# contrast_p2 = np.array([0.231, 0.289, 0.300, 0.346, 0.347, 0.286, 0.179, 0.057, 0.019, 0.057, 0.179, 
#                      0.362, 0.464, 0.486, 0.5, 0.414, 0.359, 0.354])

contrast_eraser = np.array([0.35, 0.365, 0.36, 0.308, 0.307, 0.302, 0.234, 0.181, 0.131, 0.078, 0.038, 0.062, 0.116, 0.169, 0.225, 0.268, 0.288, 0.365, 0.348])

plt.figure()
plt.plot(theta_eraser, contrast_eraser, '-o')
plt.show()
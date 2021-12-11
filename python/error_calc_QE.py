import numpy as np

'''
Error calculation
'''

delta_V = 0.005

angles = np.arange(0, 95, 5)

V_max = -np.array([0.78, 0.78, 0.78, 0.74, 0.88, 0.76, 0.98, 1.08, 1.12, 1.18, 1.24, 1.2, 1.06, 1.08, 0.96, 0.98, 0.96, 0.8, 0.84])
V_min = -np.array([1.62, 1.68, 1.66, 1.4, 1.66, 1.42, 1.58, 1.56, 1.46, 1.38, 1.34, 1.36, 1.34, 1.52, 1.52, 1.7, 1.74, 1.72, 1.74])

C = np.abs(np.round((V_max - V_min)/(V_max + V_min), 3))

delta_C = np.round(np.sqrt(2 * ((2 * V_min)/(V_min + V_max)**2 * delta_V)**2), 3)

print(C)
print(delta_C)

for i in range(19):

    print(f"$({angles[i]} \pm 0.05)$ & $({V_max[i]} \pm 0.005)$ & $({V_min[i]} \pm 0.005)$ & $({C[i]} \pm {delta_C[i]})$ \\\ ")
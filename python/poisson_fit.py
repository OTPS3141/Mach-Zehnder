# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 16:34:33 2021

@author: OTPS
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.special import factorial
from scipy.stats import poisson
from count_photons import count_photons, bins


# get poisson deviated random numbers
# data = np.random.poisson(2, 1000)

# # the bins should be of integer width, because poisson is an integer distribution
# bins = np.arange(11) - 0.5

photons, entries, bin_edges, patches = count_photons(70)
plt.hist(photons, bins = 5, density = True, label = "Data")

# calculate bin centres
bin_middles = 0.5 * (bin_edges[1:] + bin_edges[:-1])


def fit_function(k, lamb):
    '''poisson function, parameter lamb is the fit parameter'''
    return poisson.pmf(k, lamb)


# fit with curve_fit
parameters, cov_matrix = curve_fit(fit_function, bin_middles, entries)

# plot poisson-deviation with fitted parameter
x_plot = np.arange(0, 20)

plt.plot(
    x_plot,
    fit_function(x_plot, *parameters),
    marker='o', linestyle='',
    label='Fit result',
)
plt.title(f"Histogram for {70} bins with duration {np.round(500 / 70, 2)} ms")
plt.legend()
plt.show()
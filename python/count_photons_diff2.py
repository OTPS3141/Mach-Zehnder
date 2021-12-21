import numpy as np
import matplotlib.pyplot as plt
from read_bin_2 import read2
from scipy.optimize import curve_fit
from scipy.special import factorial
from scipy.stats import poisson
import matplotlib.ticker as mticker

data_list = []

for i in range(1,5):

    data_list.append(read2(f"Data\Photon statistics\statistics\pm_pos{i+1}_1\pm_pos{i+1}_1_1.csv"))

'''
Read data from statistics
'''

time, B = data_list[0].read_data2()

N = time.size

print(f"We have {N} observations")


def count(PM):
    '''
    Counts the photons from PM signal
    '''

    N = PM.size

    counter = np.zeros(N)


    for i in range(N):

        if PM[i] >= 20:

            counter[i] = 1


    photon = 0

    for i in range(1, N):

        if counter[i] == 1 and counter[i-1] == 0:

            photon += 1

    return photon

photons = count(B)

print(f"We count {photons} photons")


def bins(n):

    bins = []

    a = 0
    b = (N // n) - 1

    for i in range(0, n):



        bins.append(B[a:b])

        # print(a, b)
        a = b + 1
        b = b + (N // n)

        

    return bins

def count_bins(PM, n):

    counter_bin = []

    for i in range(n):

        counter_bin.append(count(bins(n)[i]))

    photons = np.array(counter_bin)

    return photons



'''
Compare different amount of bins
'''

def different_bins():


    for i in [5, 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100, 150]:

        photons = count_bins(bins(i), i)
        print(f"Mean: {np.mean(photons)} and std. deviation: {np.std(photons)} for {i} bins")
        plt.figure()
        plt.hist(photons, bins = i, density = False, label = "Data")
        plt.title(f"Histogram for {i} bins with duration {np.round(1000 / i, 2)} ms")

    plt.show()

# different_bins()

# print(count(bins(30)[0]))

'''
Fit to poissonian distribution
'''

def fit(n):


    gamma = count_bins(bins(n), n)

    ### What is the suitable number of bins?

    values = np.unique(gamma)
    number_of_bins = np.unique(gamma).size
    min = np.min(np.unique(gamma))
    max = np.max(np.unique(gamma))
    x_plot = np.arange(min, max + 1)
    mean = np.round(np.mean(gamma), 3)
    std = np.round(np.std(gamma), 3)


    # print(number_of_bins)

    entries, bin_edges, patches = plt.hist(gamma, bins=x_plot, density=True, label='Histogram of events', align='mid')

    # print(f"For {n} bins:")

    # print(f"Values {values} and entries {entries}")

    bin_middles = 0.5 * (bin_edges[1:] + bin_edges[:-1])

    # print(f"Bin middles {bin_middles} and bin edges {bin_edges}")

    def fit_function(k, lamb):
        '''poisson function, parameter lamb is the fit parameter'''
        return lamb**k / factorial(k) * np.exp(-lamb)

    x_plot = np.arange(min, max + 1)


    # fit with curve_fit
    parameters, cov_matrix = curve_fit(fit_function, bin_middles, entries)
    std_fit = np.sqrt(np.diag(cov_matrix))

    # print(f"Mean ({mean}, {parameters[0]}) and std. deviation ({std}, {std_fit[0]})")

    print(f"{n} & $({mean} \pm {std})$ & $({np.round(parameters[0], 3)} \pm {np.round(std_fit[0], 3)})$ \\\\")
    
    plt.plot(
        x_plot,
        fit_function(x_plot, *parameters),
        '-o',
        label='Fitting to Poissonian'
    )
    plt.title(f"Histogram for {n} bins with $\mu = {mean}$ and $\sigma = {std}$")
    # plt.text(min, np.max(entries), f"$\mu = {mean}$ and $\sigma = {std}$")
    plt.gca().xaxis.set_major_locator(mticker.MultipleLocator(1))
    plt.xlabel("Number of events (photons)")
    plt.ylabel("Probability density")
    plt.legend(loc="best")
    

# , 60, 70, 80, 90, 100, 125, 150, 175
for i in [15, 20, 30, 40, 50 , 60, 70, 80, 90, 100, 125, 150, 175]:
    plt.figure()
    fit(i)

plt.show()
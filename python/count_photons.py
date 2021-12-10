import numpy as np
import matplotlib.pyplot as plt
from read_bin import read, plot

'''
Read data from statistics
'''

df = read("Data\Photon statistics\statistics\pm_pos1_1\pm_pos1_1_1.csv")
time, A, B = df.read_data()


# plot(time, A, B)

# Number of observations
N = time.size


'''
Split the 1000 ms in n equal bins 
'''

def bins(n):
    
    bins = []
    
    a = 0
    b = (N // n) - 1
    
    for i in range(0, n):
        
        
        
        bins.append(A[a:b])
        
        a = b + 1
        b = b + (N // n)
        
        # print(a, b)
    
    return bins

# print(bins(100)[89].size)


'''
Which values does the TTL signal take?
'''
# def values_in_TTL(N):

#     values =[0]

#     for i in range(N):

#         value = B[i]

#         if np.any(value == values):
#             values.append(value)

#     return values

# values = values_in_TTL(1000)
    
# print(B)


# def find_photon_thresh():
    
#     counts = np.zeros(np.linspace(5.3, 6, 100).size)


#     for n, b in enumerate(np.linspace(5.3, 6, 100)):
        
#         counter = 0
#         # print(n, b)
    
#         for i in range(0, 976567):
            
#             if B[i] > b:
#                 counter += 1
            
#         counts[n] = counter  
    
#     return counts

# counts = find_photon_thresh()
    
# plt.plot(np.linspace(5.3, 6, 100), counts, 'o')

# good_cut = np.where(counts < 2000)
# good_cut = min(good_cut)

# print(*["Count TTL signals above",np.linspace(5.3, 6, 100)[good_cut][0]," as photon detection"])

# print(*["We have", counts[good_cut][0],"photon detections over 500 ms"])


### threshold: 5.36 V



'''
Count photons in each bin
'''

### Count the TTL rectangles

def count_TTL(TTL):

    counter = 0

    for i in range(N):

        if TTL[i] == 0:
            counter += 1

    return counter

print(count_TTL(A), "TTL rectangles were counted")


### Count the TTL rect in bins

def count_bins(n):
    
    counter_bin = []
    
    for i in range(0, n):
        
        counter = 0 
        
    
        
        for j in range(0, (N // n) - 1):
            
            if bins(n)[i][j] == 0:
                
                counter += 1
    
        counter_bin.append(counter)
    
    photons = np.array(counter_bin)
    
    plt.figure()
    entries, bin_edges, patches = plt.hist(photons, bins = n, density = True, label = "Data")
    plt.title(f"Histogram for {n} bins with duration {np.round(1000 / n, 2)} ms")
    plt.show()
    
    mean = np.mean(photons)
    
    sigma = np.std(photons)
    
    print(*["Mean:", mean, " and standard deviation:", sigma, "for", n, "bins"])
    
    
    return photons, entries, bin_edges, patches

count_bins(5)


# photons, entries, bin_edges, patches = count_bins(30) 
# '''
# Compare different amount of bins
# '''
# for i in [5, 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
    
#     count_bins(i)

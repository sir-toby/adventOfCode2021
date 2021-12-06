import numpy as np

filename = 'C:\\Users\\tbachmann\\Desktop\\Advent of coding\\2021_3.txt'

data = np.loadtxt(filename, dtype=str)
sums = [0]*len(data[0])

epsilon = ''
gamma = ''

for line in data:
    for j in range(len(line)):
        if int(line[j]) == 1:
            sums[j]+=1

for i in range(len(sums)):
    if sums[i]>len(data)/2:
        epsilon = epsilon + '1'
        gamma = gamma + '0'
    else:
        epsilon = epsilon + '0'
        gamma = gamma + '1'
    
epsilon = int(epsilon, base=2)
gamma = int(gamma, base=2)
result = epsilon*gamma


print(result, epsilon, gamma)

    

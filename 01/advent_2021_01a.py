import numpy as np
filename = '2021_1.txt'

data = np.loadtxt(filename, delimiter='\n')
datalist = data.tolist()
print(datalist)

window = 3
increase = 0
i = 0

for i in range(len(datalist)-window):
    firstvalue = sum(datalist[i:i+window])
    secondvalue= sum(datalist[i+1:i+1+window])
    
    if secondvalue>firstvalue:
        increase += 1
    
print(increase)

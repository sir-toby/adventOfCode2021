import numpy as np
import pdb

def life(datalist, oxygen):
    
    for i in range(len(datalist[0])):
        data2 = []
        letter = 0
        for line in datalist:
            letter +=int(line[i])
        if oxygen == 'oxygen':
            if letter >= (len(datalist))/2:
                select = '1'
            else: select = '0'
        elif oxygen == 'co2':
            print(letter/len(datalist))
            if letter < (len(datalist))/2:
                select = '1'
            else: select = '0'
        for line in datalist:
            if line[i] == str(select):
                data2.append(line)
        datalist = data2
    return(datalist) 


filename = 'C:\\Users\\tbachmann\\Desktop\\Advent of coding\\2021_3.txt'

data = np.loadtxt(filename, dtype=str)

##sums = [(0,0)]*len(data[0])
##oxygen = ''
##co2 = ''

##epsilon = ''
##gamma = ''
##
##for line in data:
##    for j in range(len(line)):
##        sums[j] += int(line[j])
##
##for i in range(len(sums)):
##    if sums[i]>len(data)/2:
##        epsilon = epsilon + '1'
##        gamma = gamma + '0'
##    else:
##        epsilon = epsilon + '0'
##        gamma = gamma + '1'
##    
##epsilon = int(epsilon, base=2)
##gamma = int(gamma, base=2)
##result = int(epsilon, base=2)*int(gamma, base=2)
##
##print(result)

#Part2

oxygen = life(data, 'oxygen')
co2 = life(data, 'co2')
result = int(oxygen[0], 2)*int(co2[0], 2)

print(oxygen, co2, result)

        
        
        

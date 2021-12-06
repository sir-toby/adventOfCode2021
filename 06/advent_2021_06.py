import numpy as np

def part2(fishdata, days):
    fish = [0]*9
  
    for i in range(len(fish)):
        fish[i] = fishdata.count(i)

    for day in range(0, days):
        fish_new = [0]*9
        for i in range(len(fish)):
            if i == 0:
                fish_new[8] = fish[0]
                fish_new[6] = fish[0]
            else: 
                fish_new[i-1] += fish[i]
        fish = fish_new

        
    return sum(fish)


filename = 'C:\\Users\\tbachmann\\Desktop\\Advent of coding\\2021_6.txt'
days = 256

datalist = list(map(int, np.loadtxt(filename, dtype=str, delimiter=',').tolist()))

print(part2(datalist, days))

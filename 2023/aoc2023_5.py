import time

# Reading input
start = time.time()
f= open('C:/Users/Graaheuk/Desktop/AOC/2023/input.dat','r')
lines = f.readlines()
end = time.time()
print("Time to read the file : " + str(end - start))

# Solution
solutionStart = time.time()

seeds = lines[0].split(': ')[1].split(' ')

def applyConversion(seed, convList):
    for converter in convList:
        toAdd = 0
        for i in range(len(converter)):
            if converter[i][1] <= seed and seed < converter[i][1] + converter[i][2]:
                toAdd = -(converter[i][1] - converter[i][0])
            if converter[i][1] > seed and seed >= converter[i][1] + converter[i][2]:
                toAdd = converter[i][1] - converter[i][0]
        seed += toAdd
    return seed

convertersList, converter = [], []
i = 3
while i < len(lines) and lines[i][-1] == '\n':
    if lines[i] == '\n':
        i += 1
    elif 'map' in lines[i]:
        convertersList += [converter]
        converter = []
        i += 1
    else:
        numbers = lines[i].split(' ')
        converter += [(int(numbers[0]),int(numbers[1]),int(numbers[2]))]
        i += 1
convertersList += [converter]

tmp = []
for seed in seeds:
    tmp += [applyConversion(int(seed),convertersList)]


print("Part 1 : ", min(tmp))
end = time.time()
print("Solution 1 time : " + str(end - solutionStart))
solution2Start = time.time()

seeds = lines[0].split(': ')[1].split(' ')

# PART 2
newSeeds = []
for i in range(1,len(seeds),2):
    for j in range(int(seeds[i])):
        newSeeds += [int(seeds[i-1])+j]

print(newSeeds)
seeds = newSeeds
convertersList, converter = [], []
i = 3
while i < len(lines) and lines[i][-1] == '\n':
    if lines[i] == '\n':
        i += 1
    elif 'map' in lines[i]:
        convertersList += [converter]
        converter = []
        i += 1
    else:
        numbers = lines[i].split(' ')
        converter += [(int(numbers[0]),int(numbers[1]),int(numbers[2]))]
        i += 1
convertersList += [converter]

tmp = []
for seed in seeds:
    tmp += [applyConversion(int(seed),convertersList)]


print("Part 2 : ", min(tmp))
end = time.time()
print("Solution 2 time : " + str(end - solution2Start))
print("Total time : " + str(end - start))
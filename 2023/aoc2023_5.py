import time

# Reading input
start = time.time()
f= open('C:/Users/Graaheuk/Desktop/AOC/2023/input.dat','r')
lines = f.readlines()
end = time.time()
print("Time to read the file : " + str(end - start))

# Solution
solutionStart = time.time()

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

seeds = lines[0].split(': ')[1].split(' ')

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

def applyConversionToRange(seedRange, converter):
    for i in range(len(converter)):
        if converter[i][1] <= seedRange[0] and seedRange[0] < converter[i][1] + converter[i][2] and converter[i][1] <= seedRange[1] and seedRange[1] < converter[i][1] + converter[i][2]:
            toAdd = -(converter[i][1] - converter[i][0])
            return [(seedRange[0] + toAdd, seedRange[1] + toAdd)]
        if converter[i][1] >= seedRange[0] and seedRange[0] > converter[i][1] + converter[i][2] and converter[i][1] >= seedRange[1] and seedRange[1] > converter[i][1] + converter[i][2]:
            toAdd = (converter[i][1] - converter[i][0])
            return [(seedRange[0] + toAdd, seedRange[1] + toAdd)]
        if converter[i][1] <= seedRange[0] and seedRange[0] < converter[i][1] + converter[i][2] and converter[i][1] + converter[i][2] <= seedRange[1]:
            toAdd = -(converter[i][1] - converter[i][0])
            return [(seedRange[0] + toAdd, converter[i][1] + converter[i][2] + toAdd)] + applyConversionToRange((converter[i][1] + converter[i][2] + 1, seedRange[1]), converter)
        if converter[i][1] >= seedRange[0] and converter[i][1] >= seedRange[1] and seedRange[1] > converter[i][1] + converter[i][2]:
            toAdd = (converter[i][1] - converter[i][0])
            return applyConversionToRange((seedRange[0], converter[i][1] + converter[i][2]), converter) + [(converter[i][1] + converter[i][2] + toAdd + 1, seedRange[1] + toAdd)]
        if converter[i][1] >= seedRange[0] and seedRange[1] > converter[i][1] + converter[i][2]:
            return applyConversionToRange((seedRange[0], converter[i][1]), converter) + [(converter[i][1], converter[i][1] + converter[i][2])] + applyConversionToRange((converter[i][1] + converter[i][2] + 1, seedRange[1]), converter) 
    return [seedRange]

seeds = lines[0].split(': ')[1].split(' ')

newSeeds = []
for i in range(1,len(seeds),2):
    newSeeds += [(int(seeds[i-1]),int(seeds[i-1])+int(seeds[i]))]

seedRange = newSeeds
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

def flat_list(inputList):
    res = []
    for item in inputList:
        if item is list:
            for sub in item:
                res.append(sub)
        else:
            res.append(item)
    return res

plop=seedRange
for i in range(len(convertersList)):
    tmp = []
    for seed in plop:
        tmp += applyConversionToRange(seed,convertersList[i])
    #plop = tmp
    plop = flat_list(tmp)
    i += 1

tmp = []
for range in plop:
    tmp.append(range[0])
tmp.sort()

print("Part 2 : ", tmp[0]-1)
end = time.time()
print("Solution 2 time : " + str(end - solution2Start))
print("Total time : " + str(end - start))
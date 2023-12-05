import time

# Reading input
start = time.time()
f= open('C:/Users/Ian/Downloads/aoc/2023/input.dat','r')
lines = f.readlines()
end = time.time()
print("Time to read the file : " + str(end - start))

# Solution
solutionStart = time.time()

seeds = lines[0].split(': ')[1].split(' ')

def applyConversion(seed, convList):
    for converter in convList:
        print(seed)
        toAdd = 0
        for i in range(len(converter)):
            print(converter[i])
            if converter[i][0] <= seed and seed < converter[i][1]:
                toAdd = converter[i][2]
            if converter[i][0] > seed and seed > converter[i][1]:
                toAdd = -converter[i][2]
        seed += toAdd
    return seed

converters, converter = [], []
i = 3
while i < len(lines) and lines[i][-1] == '\n':
    if lines[i] == '\n':
        i += 1
    elif 'map' in lines[i]:
        converters += [converter]
        converter = []
        i += 1
    else:
        numbers = lines[i].split(' ')
        converter += [(int(numbers[0]),int(numbers[1]),int(numbers[2]))]
        i += 1
converters += [converter]

print(converters)
tmp = []
for seed in seeds:
    tmp += [applyConversion(int(seed),converters)]


print('converters -> ', tmp)
print("Part 1 : ", tmp)
end = time.time()
print("Solution 1 time : " + str(end - solutionStart))
solution2Start = time.time()


print("Part 2 : ", )
end = time.time()
print("Solution 2 time : " + str(end - solution2Start))
print("Total time : " + str(end - start))
import time

# Reading input
start = time.time()
f= open('C:/Users/Graaheuk/Desktop/AOC/2021/3/input.dat','r')
lines = f.readlines()
end = time.time()
print("Time to read the file : " + str(end - start))

# Solution
solutionStart = time.time()

def findOccurances(lines):
    occurances = []
    for char in lines[0].strip():
        if char == '0':
            occurances += [(1,0)]
        else:
            occurances += [(0,1)]

    for line in lines[1:]:
        for i in range(len(line.strip())):
            if line[i] == '0':
                occurances[i] = (occurances[i][0]+1,occurances[i][1])
            else:
                occurances[i] = (occurances[i][0],occurances[i][1]+1)
    return occurances

occurances = findOccurances(lines)

gamma, epsilon = '', ''
for zero, un in occurances:
    if zero < un:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

power = int(gamma, 2) * int(epsilon, 2)
print("Part 1 : ", power)

print(occurances)

step = lines
tmpOxy = []
i = 0
while len(step) != 1:
    occurances = findOccurances(step)
    if occurances[i][0] > occurances[i][1]:
        most = '0'
        few = '1'
    else:
        most = '1'
        few = '0'
    for line in step:
        if line[i] == most:
            tmpOxy += [line]
    step = tmpOxy
    tmpOxy = []
    i += 1
oxyRate = step[0]

step = lines
tmpCO2 = []
i = 0
while len(step) != 1:
    occurances = findOccurances(step)
    if occurances[i][0] > occurances[i][1]:
        few = '1'
    else:
        few = '0'
    for line in step:
        if line[i] == few:
            tmpCO2 += [line]
    step = tmpCO2
    tmpCO2 = []
    i += 1
co2Rate = step[0]

print("Part 2 : ", int(oxyRate,2) * int(co2Rate,2))

end = time.time()
print("Solution time : " + str(end - solutionStart))
print("Total time : " + str(end - start))
import time
import os
import sys

# Reading input
start = time.time()

file_path = os.path.dirname(sys.argv[0])
f= open(file_path + '/input.dat','r')
lines = f.readlines()
end = time.time()
print("Time to read the file : " + str(end - start))

# Solution
solutionStart = time.time()

sum = 0
for line in lines:
    tmp = ''.join(filter(str.isdigit, line))
    sum += int(tmp[0]+tmp[-1])
    
print("Part 1 : ", sum)

REPLACEMENTS = [("one", 1),("two", 2),("three", 3),("four", 4),("five", 5),("six", 6),("seven", 7),("eight", 8),("nine", 9)]

def findFirstDigit(line):
    for i in range(len(line)):
        if line[i].isdigit():
            return int(line[i])
        else:
            for old, new in REPLACEMENTS:
                if line[i:i+len(old)] == old:
                    return new

def findLastDigit(line):
    found=False
    for i in range(len(line)-1,-1,-1):
        if line[i].isdigit():
            found=True
            return int(line[i])
        else:
            for old, new in REPLACEMENTS:
                if line[i:i+len(old)] == old:
                    found=True
                    return new
    if not found:
        return findFirstDigit(line)

sum = 0
for line in lines:
    sum += findFirstDigit(line)*10 + findLastDigit(line)
    
print("Part 2 : ", sum)

end = time.time()
print("Solution time : " + str(end - solutionStart))
print("Total time : " + str(end - start))

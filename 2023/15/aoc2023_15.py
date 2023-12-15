import time
import os
import sys

# Reading input
start = time.time()

file_path = os.path.dirname(sys.argv[0])
f = open(file_path + '/input.dat','r')
input = f.read().strip().split(',')
end = time.time()
print("Time to read the file : " + str(end - start))
solutionStart = time.time()
# Solution 1

def doHash(input):
    toAdd = 0
    for j in input:
        toAdd = ((toAdd + ord(j)) * 17) % 256
    return toAdd
sum = 0
for i in input:
    sum += doHash(i)

print("Part 1 : ", sum)
end = time.time()
print("Solution 1 time : " + str(end - solutionStart))
solution2Start = time.time()
# Solution 2

boxes = [[] for i in range(256)]
for cmd in input:
    if cmd[-1] == '-':
        tag = cmd[:-1]
        h = doHash(tag)
        boxes[h] = [(n,v) for (n,v) in boxes[h] if n!=tag]
    elif cmd[-2] == '=':
        tag = cmd[:-2]
        h = doHash(tag)
        len_ = int(cmd[-1])
        if tag in [n for (n,v) in boxes[h]]:
            boxes[h] = [(n, len_ if tag==n else v) for (n,v) in boxes[h]]
        else:
            boxes[h].append((tag, len_))

sum = 0
for i,box in enumerate(boxes):
    for j,(n,v) in enumerate(box):
        sum += (i + 1) * (j + 1) * v


print("Part 2 : ", sum)
end = time.time()
print("Solution 2 time : " + str(end - solution2Start))
print("Total time : " + str(end - start))
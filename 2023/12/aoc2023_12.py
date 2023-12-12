import time
import os
import sys

# Reading input
start = time.time()

file_path = os.path.dirname(sys.argv[0])
f = open(file_path + '/input.dat','r')
lines = f.readlines()
end = time.time()
print("Time to read the file : " + str(end - start))
solutionStart = time.time()
# Solution 1


print("Part 1 : ", )
end = time.time()
print("Solution 1 time : " + str(end - solutionStart))
solution2Start = time.time()
# Solution 2


print("Part 2 : ", )
end = time.time()
print("Solution 2 time : " + str(end - solution2Start))
print("Total time : " + str(end - start))
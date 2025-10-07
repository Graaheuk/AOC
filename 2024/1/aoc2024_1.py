import time
import os
import sys

# Reading input
start = time.time()

file_path = os.path.dirname(sys.argv[0])
f = open('C:/Users/Graaheuk/Desktop/AOC/2024/1/input.dat','r')
lines = f.readlines()
end = time.time()
print("Time to read the file : " + str(end - start))
solutionStart = time.time()
# Solution 1
list_a, list_b = [], []

for i in lines:
    a,b = i.split("   ")
    list_a.append(int(a))
    list_b.append(int(b))

list_a.sort()
list_b.sort()

res = 0
for i in range(len(list_a)):
    res += abs(list_a[i] - list_b[i])

print("Part 1 : ", res)
end = time.time()
print("Solution 1 time : " + str(end - solutionStart))

solution2Start = time.time()
# Solution 2
res = 0 
for i in range(len(list_a)):
    res += list_b.count(list_a[i]) * list_a[i]
    
print("Part 2 : ", res)

end = time.time()
print("Solution 2 time : " + str(end - solution2Start))
print("Total time : " + str(end - start))

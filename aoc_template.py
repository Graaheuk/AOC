import time

# Reading input
start = time.time()
f= open('C:/Users/Graaheuk/Desktop/AOC/2023/input.dat','r')
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
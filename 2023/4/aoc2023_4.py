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

totalScore = 0
for line in lines:
    num = line.split(': ')[1].split(' | ')
    cardNumberWin = num[0]
    cardNumberToCheck = num[1]

    tmp = []
    for i in range(0,len(cardNumberWin)-1,3):
        tmp += [int(cardNumberWin[i]+cardNumberWin[i+1])]
    cardNumberWin = tmp
    
    tmp = []
    for i in range(0,len(cardNumberToCheck)-1,3):
        tmp += [int(cardNumberToCheck[i]+cardNumberToCheck[i+1])]
    cardNumberToCheck = tmp

    score = 0
    for number in cardNumberToCheck:
        if number in cardNumberWin:
            score += 1
    totalScore += int(2**(score-1))

print("Part 1 : ", totalScore)
end = time.time()
print("Solution 1 time : " + str(end - solutionStart))
solution2Start = time.time()

totalScore = []
for line in lines:
    totalScore += [(line.split(': ')[0].split(' ')[1], 1)]

i=0
for i in range(len(lines)):
    num = lines[i].split(': ')[1].split(' | ')
    cardNumberWin = num[0]
    cardNumberToCheck = num[1]

    tmp = []
    for h in range(0,len(cardNumberWin)-1,3):
        tmp += [int(cardNumberWin[h]+cardNumberWin[h+1])]
    cardNumberWin = tmp
    tmp = []
    for h in range(0,len(cardNumberToCheck)-1,3):
        tmp += [int(cardNumberToCheck[h]+cardNumberToCheck[h+1])]
    cardNumberToCheck = tmp
    
    score = 0
    for number in cardNumberToCheck:
        if number in cardNumberWin:
            score += 1
    for j in range(1, score+1):
        totalScore[i+j] = (totalScore[i+j][0],totalScore[i+j][1]+totalScore[i][1])
sum=0
for score in totalScore:
    sum += score[1]
    
print("Part 2 : ", sum)
end = time.time()
print("Solution 2 time : " + str(end - solution2Start))
print("Total time : " + str(end - start))
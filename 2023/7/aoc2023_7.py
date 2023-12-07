import time
import os
import sys
import itertools

# Reading input
start = time.time()

file_path = os.path.dirname(sys.argv[0])
f = open(file_path + '/input.dat','r')
lines = f.readlines()
end = time.time()
print("Time to read the file : " + str(end - start))
solutionStart = time.time()
# Solution 1

CARDS = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
CARD_ORDER = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, 'T': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12}

def isFive(cards):
    return cards[0]==cards[1] and cards[1]==cards[2] and cards[2]==cards[3] and cards[3]==cards[4]

def isFour(cards):
    for value in CARDS:
        if cards.count(value)==4:
            return True
    return False

def isFull(cards):
    for value in CARDS:
        if cards.count(value)==3:
            for fullValue in CARDS:
                if cards.count(fullValue)==2:
                    return True
    return False

def isThree(cards):
    for value in CARDS:
        if cards.count(value)==3:
            return True
    return False

def isTwoPair(cards):
    first=''
    for value in CARDS:
        if cards.count(value)==2:
            first = value
            for value in CARDS:
                if cards.count(value)==2 and value != first:
                    return True
    return False

def isPair(cards):
    for value in CARDS:
        if cards.count(value)==2:
            return True
    return False


count = [[],[],[],[],[],[],[]]
for line in lines:
    hand, bid = line.split(' ')
    round = (hand, bid.strip())
    if isFive(round[0]):
        count[0] = [round] + count[0]
    elif isFour(round[0]):
        count[1] = [round] + count[1]
    elif isFull(round[0]):
        count[2] = [round] + count[2]
    elif isThree(round[0]):
        count[3] = [round] + count[3]
    elif isTwoPair(round[0]):
        count[4] = [round] + count[4]
    elif isPair(round[0]):
        count[5] = [round] + count[5]
    else:
        count[6] = [round] + count[6]
    
print(count)
def flat_list(inputList):
    res = []
    for item in inputList:
        if item is list or item == []:
            if len(item) > 0:
                item = list(dict.fromkeys(item[::-1]))
                item = item.sort(key=lambda val: CARD_ORDER[val[1]])
                for sub in item:
                    res = [sub] + res
        else:
            res.append(item)
    return res

sortedHands = flat_list(count)
print(count)
sortedHands=list(itertools.chain.from_iterable(count))
print(sortedHands)
score = 0
for i in range(len(sortedHands)):
    score += (i + 1) * int(sortedHands[i][1])

print("Part 1 : ", score)
end = time.time()
print("Solution 1 time : " + str(end - solutionStart))
solution2Start = time.time()
# Solution 2









print("Part 2 : ", )
end = time.time()
print("Solution 2 time : " + str(end - solution2Start))
print("Total time : " + str(end - start))
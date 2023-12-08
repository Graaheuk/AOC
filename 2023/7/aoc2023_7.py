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

CARDS = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']

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

def sort_and_flat_list(inputList):
    res = []
    for item in inputList:
        if len(item) > 1:
            Tribulle(item)
            res = item + res
        elif len(item) == 1:
            res = item + res
    return res

# LULU
listforcestr='23456789TJQKA'

def Tribulle(listmain) :
    l = len(listmain)
    for t in range(l-1):
        main1=listmain[0][0]
        iold=0
        for i in range(1,l):
            if Ordre(main1,listmain[i][0]) == 2:
                listmain.insert(i,listmain[iold])
                del(listmain[iold])
                iold=i
                main1=listmain[i][0]
            elif i == l-1:
                listmain.insert(i+1,listmain[iold])
                del(listmain[iold])
        l-=1

def Ordre(main1,main2):
    for i in range(5):
        if listforcestr.index(main1[i]) > listforcestr.index(main2[i]):
            return 1
        elif listforcestr.index(main1[i]) < listforcestr.index(main2[i]):
            return 2
    return 2 
# LULU

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

sortedHands = sort_and_flat_list(count)
score = 0
for i in range(len(sortedHands)):
    score += (i + 1) * int(sortedHands[i][1])

print("Part 1 : ", score)
end = time.time()
print("Solution 1 time : " + str(end - solutionStart))
solution2Start = time.time()
# Solution 2

def isFive2(cards):
    if 'J' in cards:
        cardsTmp = cards[:cards.index('J')]+cards[cards.index('J')+1:]
        return isFour2(cardsTmp)
    else:
        return isFive(cards)

def isFour2(cards):
    if 'J' in cards:
        cardsTmp = cards[:cards.index('J')]+cards[cards.index('J')+1:]
        return isThree2(cardsTmp)
    else:
        return isFour(cards)

def isFull2(cards):
    if 'J' in cards:
        cardsTmp = cards[:cards.index('J')]+cards[cards.index('J')+1:]
        return isTwoPair2(cardsTmp)
    else: 
        return isFull(cards)

def isThree2(cards):
    if 'J' in cards:
        cardsTmp = cards[:cards.index('J')]+cards[cards.index('J')+1:]
        return isPair2(cardsTmp)
    else:
        return isThree(cards)

def isTwoPair2(cards):
    if 'J' in cards:
        cardsTmp = cards[:cards.index('J')]+cards[cards.index('J')+1:]
        return isPair2(cardsTmp)
    else:
        return isTwoPair(cards)

def isPair2(cards):
    if 'J' in cards:
        return True
    else:
        return isPair(cards)

def sort_and_flat_list2(inputList):
    res = []
    for item in inputList:
        if len(item) > 1:
            Tribulle2(item)
            res = item + res
        elif len(item) == 1:
            res = item + res
    return res

# LULU
listforcestr2='J23456789TQKA'

def Tribulle2(listmain) :
    l = len(listmain)
    for t in range(l-1):
        main1=listmain[0][0]
        iold=0
        for i in range(1,l):
            if Ordre2(main1,listmain[i][0]) == 2:
                listmain.insert(i,listmain[iold])
                del(listmain[iold])
                iold=i
                main1=listmain[i][0]
            elif i == l-1:
                listmain.insert(i+1,listmain[iold])
                del(listmain[iold])
        l-=1

def Ordre2(main1,main2):
    for i in range(5):
        if listforcestr2.index(main1[i]) > listforcestr2.index(main2[i]):
            return 1
        elif listforcestr2.index(main1[i]) < listforcestr2.index(main2[i]):
            return 2
    return 2 
# LULU

count = [[],[],[],[],[],[],[]]
for line in lines:
    hand, bid = line.split(' ')
    round = (hand, bid.strip())
    if isFive2(round[0]):
        count[0] = [round] + count[0]
    elif isFour2(round[0]):
        count[1] = [round] + count[1]
    elif isFull2(round[0]):
        count[2] = [round] + count[2]
    elif isThree2(round[0]):
        count[3] = [round] + count[3]
    elif isTwoPair2(round[0]):
        count[4] = [round] + count[4]
    elif isPair2(round[0]):
        count[5] = [round] + count[5]
    else:
        count[6] = [round] + count[6]

sortedHands = sort_and_flat_list2(count)

score = 0
for i in range(len(sortedHands)):
    score += (i + 1) * int(sortedHands[i][1])

print("Part 2 : ", score)

end = time.time()
print("Solution 2 time : " + str(end - solution2Start))
print("Total time : " + str(end - start))
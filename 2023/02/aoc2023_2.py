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

class Game:
    id = 0
    possible = True
    maxR, maxB, maxG = 0, 0, 0

    def __init__(self, id):
        self.id = id

    def addGameSet(self, r, g, b):
        if r > self.maxR:
            self.maxR = r
        if g > self.maxG:
            self.maxG = g
        if b > self.maxB:
            self.maxB = b
        if r > 12 or g > 13 or b > 14:
            self.possible = False

    def getPower(self):
        return self.maxR * self.maxG * self.maxB

# Solution
solutionStart = time.time()

gameList = []

for line in lines:
    gameSplit = line.split(': ')

    game = Game(int(gameSplit[0][5:]))
    for gameSet in gameSplit[1].split('; '):
        colors = gameSet.split(', ')
        r, g, b = 0, 0, 0
        for color in colors:
            colorSplit = color.split(' ')
            if('red' in color):
                r = int(colorSplit[0])
            if('green' in color):
                g = int(colorSplit[0])
            if('blue' in color):
                b = int(colorSplit[0])
        game.addGameSet(r, g, b)
    #if game.possible:
    gameList += [game]

sum = 0
for game in gameList:
    sum += game.getPower()

print("Part 2 : ", sum)

end = time.time()
print("Solution 2 time : " + str(end - solutionStart))
print("Total time : " + str(end - start))
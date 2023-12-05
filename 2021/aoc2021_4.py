import time

# Reading input
start = time.time()
f= open('C:/Users/Graaheuk/Desktop/AOC/2021/input.dat','r')
lines = f.readlines()
end = time.time()
print("Time to read the file : " + str(end - start))

# Solution
solutionStart = time.time()

class Board:
    board = []

    def __init__(self, lines):
        for line in lines:
            tmp = []
            for i in range(0,len(line)-1,3):
                tmp += [(int(line[i]+line[i+1]), False)]
            self.board += [tmp]
        
    def isWinning(self):
        winning = False
        for g in range(len(self.board[0])):
            print(g)
            winning = winning or (self.board[0][g] and self.board[1][g] and self.board[2][g] and self.board[3][g] and self.board[4][g])
            winning = winning or (self.board[g][0] and self.board[g][1] and self.board[g][2] and self.board[g][3] and self.board[g][4])
        return winning
    
    def validateNumber(self, hit):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j][0] == hit:
                    self.board[i][j] = (self.board[i][j][0],True)


def checkBoardWin(boards):
    for i in range(len(boards)):
        if boards[i].isWinning():
            return i
    return -1

boards = []
for i in range(2,len(lines),6):
    boards += [Board(lines[i:i+6])]

boardId = -1
i = 0
draw = lines[0].split(',')
while boardId == -1:
    for board in boards:

        print('----------------')
        board.validateNumber(int(draw[i]))
        print(board.board)
        
    i += 1
    boardId = checkBoardWin(boards)

print("Part 1 : ", boardId)
print("Solution 1 time : " + str(end - solutionStart))
solution2Start = time.time()




print("Part 2 : ", )
end = time.time()
print("Solution 2 time : " + str(end - solution2Start))
print("Total time : " + str(end - start))
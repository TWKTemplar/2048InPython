import random
import numpy
def SpawnRandom(board):
    x = random.randrange(len(board))
    y = random.randrange(len(board))
    for i in range(5):
        if(board[x][y] == 0):
            board[x][y] = 2
            return board
    return board

def Collapse(board):

    return board

def Merge(board):

    return board
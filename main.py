
import numpy
import functions
BOARDSIZE = 4

Board = numpy.zeros((BOARDSIZE, BOARDSIZE), dtype = int)
Board = functions.SpawnRandom(Board)
print(Board)
input("Press Enter to continue...")

for i in range(10):
    Board = functions.Collapse(Board)
    Board = functions.Merge(Board)
    Board = functions.Collapse(Board)
    Board = functions.SpawnRandom(Board)
    print(Board)
    input("Press Enter to continue...")

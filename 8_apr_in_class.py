import numpy as np

num = int(input("Please enter the dimension of the board : "))

board = np.zeros((num, num))
board[::2, ::2] = 1
board [1::2, 1::2] = 1
print(board)
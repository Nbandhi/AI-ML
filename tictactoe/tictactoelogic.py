#!/usr/bin/env python
# coding: utf-8

# In[ ]:

"""
Tic Tac Toe Player
"""

# In[ ]:

import math
import copy

# In[ ]:

X = "X"
O = "O"
EMPTY = None

# In[ ]:

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


# In[1]:


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if not(terminal(board)):
        if sum([i.count(EMPTY) for i in board]) % 2 == 0:
            return O
        else:
            return X

# In[1]:


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    
    possibleActions = []
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == EMPTY:
                possibleActions.append((i, j))
    return possibleActions



# In[ ]:


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    copyBoard = copy.deepcopy(board)
    i, j = action

    if copyBoard[i][j] == EMPTY:
        copyBoard[i][j] = player(board)
        return copyBoard
    else:

        print("Invalid move")

# In[ ]:


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    b = board
    for i in range(3):
        # Checking for Rows for X or O victory.
        if (b[i][0] == b[i][1] == b[i][2]):
            if (b[i][0] == X):
                return X
            elif (b[i][0] == O):
                return O

        # Checking for Columns for X or O victory.
        elif (b[0][i] == b[1][i] == b[2][i]):
            if (b[0][i] == X):
                return X
            elif (b[0][i] == O):
                return O

    # Checking for Diagonals for X or O victory.
    if (b[0][0] == b[1][1] == b[2][2]):
        if (b[0][0] == X):
            return X
        elif (b[0][0] == O):
            return O
    elif (b[0][2] == b[1][1] == b[2][0]):
        if (b[0][2] == X):
            return X
        elif (b[0][2] == O):
            return O

    # Else if none of them have won then return None
    return None


# In[ ]:


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    availableMoves = actions(board)
    if len(availableMoves) == 0:
        return True
    if winner(board) is not None:
        return True
    return False

# In[ ]:


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

# In[ ]:

def undo(board, row, col):
    board[row][col] = EMPTY


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    alpha = -math.inf
    d = beta = math.inf

    if player(board) == X:
        bestVal = -math.inf
        for action in actions(board):
            value, depth = MIN_value(result(board,action), alpha, beta, 0)
            if value > bestVal or (value == bestVal and depth < d):
                move = action
                bestVal = value
                d = depth
    elif player(board) == O:
        bestVal = math.inf
        for action in actions(board):
            value, depth = MAX_value(result(board,action), alpha, beta, 0)
            if value < bestVal or (value == bestVal and depth < d):
                move = action
                bestVal = value
                d = depth

    return move

def MIN_value(board,alpha,beta,depth):

    if terminal(board):
        return utility(board), depth

    m = math.inf

    for action in actions(board):
        value, depth = MAX_value(result(board,action), alpha, beta, depth + 1)
        m = min(m, value)

        # alpha-beta pruning
        beta = min(beta, m)
        if beta <= alpha:
            break

    return m, depth

def MAX_value(board,alpha,beta,depth):
    if terminal(board):
        return utility(board), depth

    m = -math.inf

    for action in actions(board):
        value, depth = MIN_value(result(board, action), alpha, beta, depth + 1)
        m = max(m, value)

        # alpha-beta pruning
        alpha = max(alpha, m)
        if beta <= alpha:
            break

    return m, depth


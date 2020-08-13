"""
Tic Tac Toe Player
"""
# minimax reference: https://github.com/Cledersonbc/tic-tac-toe-minimax

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """

    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    c = count(board)
    return X if c%2==0 else O

def count(board):
    count = 0
    for j in range(3):
        count += sum(x is not None for x in board[j])
    return count

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    results = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                results.add((i,j))
    return results



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    print(action)
    board[action[0]][action[1]] = player(board)
    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    end = terminal(board)
    if end:
        if count(board) == 9 and utility(board)== 0 :
            return None
        else:
            return X if utility(board) == 1 else O



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    status = utility(board)

    if status !=0:
        return True
    elif status == 0 and count(board) == 9:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # check for winner in the same row
    for i in range(3):
        cur = board[i][0]
        match = cur != None
        for j in range(3):
            match = board[i][j] == cur and match
        if match:
            return 1 if board[i][0] == X else -1 if board[i][0] == O else 0

    # check for winner in the same column
    for i in range(3):
        cur = board[0][i]
        match = cur != None
        for j in range(3):
            match = board[j][i] == cur and match
        if match:
            return 1 if board[0][i] == X else -1 if board[0][i] == O else 0

    # check for winner in the diagnol
    cur = board[0][0]
    match = cur != None
    for i in range(3):
        match = board[i][i] == cur and match
    if match:
        return 1 if board[0][0] == X else -1 if board[0][0] == O else 0
    # check for winner in the anti-diagnol
    cur = board[2][0]
    match = cur != None
    for i in range(2,-1,-1):
        match = board[i][2-i] == cur and match
    if match:
        return 1 if board[2][0] == X else -1 if board[2][0] == O else 0

    return 0



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # next move must be AI
    AI = player(board)
    human = X if AI == O else O
    # we want to max AI gain
    _, next_move = recur_min(board,AI,human)
    return next_move


def recur_min(board,AI,human):
    this_move = player(board)
    if this_move == AI:
        best = [-999, (-1,-1)]
    else:
        best = [999, (-1,-1)]

    end = terminal(board)
    if end and winner(board) == AI:
        return [1,(-1,-1)]
    elif end and winner(board) == human:
        return [-1, (-1,-1)]
    elif end:
        return [0,(-1,-1)]

    for action in actions(board):
        moved_board = result(board,action)
        score = recur_min(moved_board,AI,human)
        board[action[0]][action[1]] = EMPTY
        score[1] = action

        if this_move == AI:
            if score[0]>best[0]:
                best = score
        else:
            if score[0]<best[0]:
                best = score
    return best


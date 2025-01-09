from search_algorithms import breadth_first_search, depth_first_search

n = 25


def is_goal(state):
    return len(state) == n


def next_states(state):
    states = []
    next_moves = [i for i in range(n) if i not in state]
    for move in next_moves:
        y = len(state)
        x = move
        if check_diagonals(x, y, state):
            new_state = state.copy()
            new_state.append(move)
            states.append(new_state)
    return states


def check_diagonals(x, y, state):
    for i in range(len(state)):
        current_y = i
        current_x = state[i]
        if abs(x - current_x) == abs(y - current_y):
            return False
    return True


queens = depth_first_search([], next_states, is_goal)
board = []
for i in range(n):
    board.append(["*"] * n)
    board[i][queens[-1][i]] = "Q"
for row in board:
    row_string = ""
    for col in row:
        row_string += col + " "
    print(row_string)

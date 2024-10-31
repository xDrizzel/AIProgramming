import copy

from search_algorithms import breadth_first_search

grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 0, 0]]


def is_goal(state):
    for i in state:
        for j in i:
            if j == 0:
                return False
    return True


def next_state(state):
    x = None
    y = None
    for i in range(9):
        for j in range(9):
            if state[i][j] == 0:
                x = j
                y = i
                break
        if x is not None:
            break
    possibilities = [i for i in range(1, 10)]
    for i in state[y]:
        if i in possibilities:
            possibilities.remove(i)
    for i in range(9):
        if state[i][x] in possibilities:
            possibilities.remove(state[i][x])
    box_index_y = y // 3 * 3
    box_index_x = x // 3 * 3
    box_numbers = []
    for i in range(3):
        for j in range(3):
            box_numbers.append(state[box_index_y + i][box_index_x + j])
    for i in box_numbers:
        if i in possibilities:
            possibilities.remove(i)
    states = []
    for i in possibilities:
        new_state = [row[:] for row in state]
        new_state[y][x] = i
        states.append(new_state)
    return states


solution = breadth_first_search(grid, next_state, is_goal)
for row in solution[-1]:
    print(row)

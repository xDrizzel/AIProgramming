import copy
import random
from search_algorithms import breadth_first_search

N = 3
goal = [[i*N+j for j in range(N)] for i in range(N)]


def is_goal(state):
    return state == goal


def next_states(state):
    r = None
    c = None
    for i in range(N):
        for j in range(N):
            if state[i][j] == 0:
                r = i
                c = j
                break
    states = []
    if r-1 >= 0:
        new_state = copy.deepcopy(state)
        new_state[r][c] = new_state[r-1][c]
        new_state[r-1][c] = 0
        states.append(new_state)
    if r+1 < N:
        new_state = copy.deepcopy(state)
        new_state[r][c] = new_state[r+1][c]
        new_state[r+1][c] = 0
        states.append(new_state)
    if c-1 >= 0:
        new_state = copy.deepcopy(state)
        new_state[r][c] = new_state[r][c-1]
        new_state[r][c-1] = 0
        states.append(new_state)
    if c+1 < N:
        new_state = copy.deepcopy(state)
        new_state[r][c] = new_state[r][c+1]
        new_state[r][c+1] = 0
        states.append(new_state)
    return states


def mk_initial():
    s = goal
    for _ in range(30):
        s = random.choice(next_states(s))
    return s


def num_digits(n):
    d = 1
    while n >= 10:
        n = n // 10
        d = d + 1
    return d


nd = num_digits(N * N - 1)


def print_state(state):
    n = nd
    for row in state:
        for cell in row:
            print(f"| {cell:>n} ", end='')
        print("|")
    print()


for s in breadth_first_search(mk_initial(), next_states, is_goal):
    print_state(s)



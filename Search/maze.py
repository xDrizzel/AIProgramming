from search_algorithms import breadth_first_search

maze = [[' ', 'W', ' ', ' ', 'G'],
        [' ', 'W', ' ', 'W', ' '],
        [' ', 'W', ' ', ' ', ' '],
        [' ', ' ', 'W', 'W', ' '],
        [' ', ' ', ' ', ' ', ' ']]

rows = len(maze)
cols = len(maze[0])


def is_goal(state):
    return maze[state[0]][state[1]] == 'G'


def next_states(state):
    states = []
    new_state = (state[0] - 1, state[1])
    if new_state[0] >= 0 and maze[new_state[0]][new_state[1]] != "W":
        states.append(new_state)
    new_state = (state[0] + 1, state[1])
    if new_state[0] < rows and maze[new_state[0]][new_state[1]] != "W":
        states.append(new_state)
    new_state = (state[0], state[1] - 1)
    if new_state[1] >= 0 and maze[new_state[0]][new_state[1]] != "W":
        states.append(new_state)
    new_state = (state[0], state[1] + 1)
    if new_state[1] < cols and maze[new_state[0]][new_state[1]] != "W":
        states.append(new_state)
    return states


print(breadth_first_search((0, 0), next_states, is_goal))

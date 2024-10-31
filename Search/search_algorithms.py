def breadth_first_search(start, next_states, is_goal):
    to_do = []
    for state in next_states(start):
        to_do.append([start, state])
    explored = []
    while to_do:
        path = to_do.pop(0)
        current = path[-1]
        if is_goal(current):
            return path
        for state in next_states(current):
            if state not in explored:
                explored.append(state)
                new_path = path.copy()
                new_path.append(state)
                to_do.append(new_path)
    raise Exception("No solution found")

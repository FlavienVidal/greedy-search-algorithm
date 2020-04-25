# # # # GREEDY SEARCH ALGORITHM # # # #


def fill_p3(x):  # action 1
    x = 3
    return x


def poor_p3_into_p5(x, y):  # action 2
    res = x+y
    if res <= 5:
        y = res
        x = 0
    if res > 5:
        y = 5
        x = res-5
    return x, y  # p3 p5


def poor_p5_into_p3(x, y):  # action 3
    res = x+y
    if res <= 3:
        x = res
        y = 0
    if res > 3:
        x = 3
        y = res-3
    return x, y  # p5 p3


def empty_p3(x):  # action 4
    x = 0
    return x


def empty_p5(x):  # action 5
    x = 0
    return x


def bfs_prob1(x, y):  # x, y are the initial volumes in P3 and P5
    IS = [x, y]  # Initial state
    frontier = [IS]
    path = []
    i = 0
    selected_node = frontier[0]
    x, y = selected_node[0], selected_node[1]
    while y != 4:  # Goal state
        "Action 1"
        x_new = fill_p3(x)
        if [x_new, y] not in frontier and [x_new, y] not in path:
            frontier.append([x_new, y])
        "Action 2"
        res = list(poor_p3_into_p5(x, y))  # converts the tuple into a list
        if res not in frontier and res not in path:
            frontier.append(res)
        "Action 3"
        res = list(poor_p5_into_p3(x, y))  # converts the tuple into a list
        if res not in frontier and res not in path:
            frontier.append(res)
        "Action 4"
        x_new = empty_p3(x)
        if [x_new, y] not in frontier and [x_new, y] not in path:
            frontier.append([x_new, y])
        "Action 5"
        y_new = empty_p5(y)
        if [x, y_new] not in frontier and [x, y_new] not in path:
            frontier.append([x, y_new])
        'Remove selected node from frontier and add it to the path'
        path.append(frontier.pop(0))
        i += 1
        print("Node", i, "  Frontier =", frontier)
        selected_node = frontier[0]
        x, y = selected_node[0], selected_node[1]
    path.append(frontier.pop(0))
    return path


def optimal_seq_of_actions_prob1(path):
    path.reverse()
    shortest_path = [path[0]]
    for i in range(1, len(path)):
        selected_node = path[i]
        x, y = selected_node[0], selected_node[1]
        'Can 1 of the 5 possible actions reach the previous state (in other words: are they successive states)'
        x_action1 = fill_p3(x)
        res_action2 = list(poor_p3_into_p5(x, y))
        res_action3 = list(poor_p5_into_p3(x, y))
        x_action4 = empty_p3(x)
        y_action5 = empty_p5(y)
        if [x_action1, y] == shortest_path[-1] or res_action2 == shortest_path[-1] or res_action3 == shortest_path[-1] or [x_action4, y] == shortest_path[-1] or [x, y_action5] == shortest_path[-1]:
            shortest_path.append(path[i])
    shortest_path.reverse()
    return shortest_path


P3_initial, P5_initial = 0, 0

path_of_the_algo = bfs_prob1(P3_initial, P5_initial)
print("The path followed by the algorithm to reach G is", path_of_the_algo)

optimal_seq_of_actions = optimal_seq_of_actions_prob1(path_of_the_algo)
print("The optimal sequence of actions is:", optimal_seq_of_actions)

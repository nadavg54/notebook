from collections import defaultdict

WHITE = 0
GRAY = 1
BLACK = 2

EDGES = [(0, 1), (1, 2), (0, 2), (2, 3), (3, 0)]

ENTER = 0
EXIT = 1

def create_graph(edges):
    graph = defaultdict(list)
    for x, y in edges:
        graph[x].append(y)

    return graph

def dfs_iter(graph, start):
    state = {v: WHITE for v in graph}
    stack = [(ENTER, start)]

    while stack:
        act, v = stack.pop()

        if act == EXIT:
            print('Exit', v)
            state[v] = BLACK
        else:
            print('Enter', v)
            state[v] = GRAY
            stack.append((EXIT, v))
            for n in graph[v]:
                if state[n] == GRAY:
                    print('Found cycle at', n)
                elif state[n] == WHITE:
                    stack.append((ENTER, n))

graph = create_graph(EDGES)
dfs_iter(graph, 0)

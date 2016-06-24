"""
Example Input:
3
10
3 5
7 8
44 56
36 54
88 91
77 83
2 4
9 99
45 78
31 75
5
10 6
95 90
96 30
97 52
98 86
2
3 54
37 100
1
56 33
1
5 6
1
97 95

Example Results
victory [1, 4, 99] [100]
3
victory [1, 54, 33] [100]
3
victory [1, 4, 10, 16, 22, 28, 34, 40, 46, 52, 58, 64, 70, 76, 82, 88, 94] [100]
17
"""

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    visited = []
    while queue:
        (vertex, path) = queue.pop(0)
        #print(vertex, path, graph[vertex])
        for nex in graph[vertex] - set(path):
            if nex in visited:
                continue
            visited.append(nex)
            if nex in l:
                nex = l[nex]
            if nex in s:
                nex = s[nex]
            if nex == goal:
                print("victory",path,[nex])
                yield path + [nex]
            else:
                queue.append((nex, path + [nex]))


def shortest_path(graph, goal, start=1):
    try:
        return len(next(bfs_paths(graph, start, goal))) - 1
    except StopIteration:
        return -1


g = {}
for i in range(100):
    x = i + 1
    g[x] = {a for a in range(x+1, x + 1 + 6)}

t = int(input())

for a0 in range(t):
    l = {}
    s = {}
    lcount = int(input())
    for a1 in range(lcount):
        x = [int(n) for n in input().split()]
        i = x[0]
        j = x[1]
        l[i] = j
    scount = int(input())
    for a2 in range(scount):
        x = [int(n) for n in input().split()]
        i = x[0]
        j = x[1]
        s[i] = j
    # l = {32: 62, 42: 68, 12: 98}
    # s = {95: 13, 97: 25, 93: 37, 79: 27, 75: 19, 49: 47, 67: 17}
    print(shortest_path(g, 100))

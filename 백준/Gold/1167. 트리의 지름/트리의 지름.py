import sys
sys.setrecursionlimit(10**5)

V = int(sys.stdin.readline())

graph = [[] * V for _ in range(V + 1)]
visited_dfs = [-1] * (V + 1)

def dfs(node, weight):
    for n, l in graph[node]:
        cost = weight + l
        if visited_dfs[n] == -1:
            visited_dfs[n] = cost
            dfs(n, cost)
    return


for i in range(1, V + 1):
    nodeinfo = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(1, len(nodeinfo), 2):
        if nodeinfo[j] == -1:
            continue
        else:
            graph[nodeinfo[0]].append((nodeinfo[j], nodeinfo[j + 1]))

        
visited_dfs[1] = 0

dfs(1, 0)

idx = visited_dfs.index(max(visited_dfs))

visited_dfs = [-1] * (V + 1)

visited_dfs[idx] = 0

dfs(idx, 0)

print(max(visited_dfs))
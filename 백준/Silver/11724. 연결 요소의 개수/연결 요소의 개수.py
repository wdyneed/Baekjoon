import sys
sys.setrecursionlimit(10 ** 6)

N, M = map(int, sys.stdin.readline().split())

arr = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

def dfs(node):
    visited[node] = 1
    for i in range(len(arr[node])):
        nextnode = arr[node][i]
        if visited[nextnode] == 0:
            dfs(nextnode)

for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    arr[u].append(v)
    arr[v].append(u)
    
count = 0

for i in range(1, N + 1):
    if visited[i] == 0:
        dfs(i)
        count += 1
        
print(count)
import sys


N, M = map(int, sys.stdin.readline().split())

result = []

def dfs(start):
    if len(result) == M:
        print(' '.join(map(str, result)))
        return

    for i in range(start, N + 1):
        result.append(i)
        dfs(i)
        result.pop()
    
dfs(1)
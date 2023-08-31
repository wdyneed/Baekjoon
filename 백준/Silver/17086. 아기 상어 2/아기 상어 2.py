import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

d = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

q = deque()

def bfs():
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if nx >= 0 and nx < N and ny >= 0 and ny < M:
                if not arr[nx][ny]:
                    arr[nx][ny] = arr[x][y] + 1
                    q.append((nx, ny))
                    

for i in range(N):
    for j in range(M):
        if arr[i][j]:
            q.append((i, j))
            

bfs()

print(max(map(max, arr)) - 1)
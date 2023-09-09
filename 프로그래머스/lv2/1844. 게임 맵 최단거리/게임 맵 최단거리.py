from collections import deque

def solution(maps):
    N = len(maps)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    q = deque()
    q.append((0, 0))
    M = len(maps[0])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and ny >= 0 and nx < N and ny < M:
                if maps[nx][ny] == 1:
                    q.append((nx, ny))
                    maps[nx][ny] = maps[x][y] + 1

    if maps[-1][-1] == 1:
        return -1
    else:
        return maps[-1][-1]
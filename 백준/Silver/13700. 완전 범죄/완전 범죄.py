import sys
from collections import deque

N, S, D, F, B, K = map(int, sys.stdin.readline().split())
police = list(map(int, sys.stdin.readline().split()))
arr = [0] * (N + 1)

for i in range(K):
    arr[police[i]] = 1


def check(cnt, x):
    queue = deque()
    queue.append((cnt, x))
    
    while queue:
        cnt, x = queue.popleft()
        dx = [x - B, x + F]
        for nx in dx:
            if nx > N or nx < 0:
                continue
            if arr[nx] == 1:
                continue
            if nx == D:
                return cnt + 1
            arr[nx] = 1
            queue.append((cnt + 1, nx))
            
    return "BUG FOUND"
            
cnt = 0

print(check(cnt, S))
        
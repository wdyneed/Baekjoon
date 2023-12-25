import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

q = deque([i for i in range(1, N + 1)])
count = 0
ordering = list(map(int, sys.stdin.readline().split()))

for num in ordering:
    while True:
        if q[0] == num:
            q.popleft()
            break
        else:
            idx = q.index(num)
            
            if idx <= len(q) // 2:
                q.append(q.popleft())
            else:
                q.appendleft(q.pop())
            count += 1
                
print(count)
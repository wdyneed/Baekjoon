import sys
from collections import deque

N = int(sys.stdin.readline())
deq = deque()

for i in range(N):
    orderline = sys.stdin.readline().split()
    order = int(orderline[0])
    
    if order == 1:
        deq.appendleft(int(orderline[1]))
    elif order == 2:
        deq.append(int(orderline[1]))
    elif order == 3:
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.popleft())
    elif order == 4:
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.pop())
    elif order == 5:
        print(len(deq))
    elif order == 6:
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif order == 7:
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
    elif order == 8:
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[-1])    
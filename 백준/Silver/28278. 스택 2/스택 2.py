import sys

N = int(sys.stdin.readline())

arr = []

for i in range(N):
    order = sys.stdin.readline().split()
    if int(order[0]) == 1:
        arr.append(int(order[1]))
    elif int(order[0]) == 2:
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.pop())
    elif int(order[0]) == 3:
        print(len(arr))        
    elif int(order[0]) == 4:
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[-1])
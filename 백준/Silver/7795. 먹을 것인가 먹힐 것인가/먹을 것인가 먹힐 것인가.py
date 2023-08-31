import sys

T = int(sys.stdin.readline())

for i in range(T):
    N, M = map(int, sys.stdin.readline().split())
    arr_A = sorted(list(map(int, sys.stdin.readline().split())))
    arr_B = sorted(list(map(int, sys.stdin.readline().split())))
    idx = 0
    res = 0
    
    for i in range(N):
        while idx < M:
            if arr_A[i] > arr_B[idx]:
                idx += 1
            else:
                break
        res += idx
    print(res)
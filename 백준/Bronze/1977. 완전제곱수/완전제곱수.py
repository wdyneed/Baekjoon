import sys

def check(n):
    return int(n ** 0.5) ** 2 == n

arr = []

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

for i in range(M, N + 1):
    if check(i) == True:
        arr.append(i)

if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(arr[0])        
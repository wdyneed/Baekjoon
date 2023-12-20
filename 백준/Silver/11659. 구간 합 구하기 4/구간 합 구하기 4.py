import sys

N, M = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

prefix = [arr[0]]

for i in range(1, N):
    prefix.append(prefix[i - 1] + arr[i])

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    if i == 1:
        print(prefix[j - 1])
    else:
        print(prefix[j - 1] - prefix[i - 2])
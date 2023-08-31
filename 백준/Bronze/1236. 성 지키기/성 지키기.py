import sys

N, M = map(int, sys.stdin.readline().split())
arr = []

for i in range(N):
    arr.append(sys.stdin.readline())

row, col = 0, 0

for i in range(N):
    if 'X' not in arr[i]:
        row += 1
        
for j in range(M):
    if 'X' not in [arr[i][j] for i in range(N)]:
        col += 1
        
print(max(col, row))
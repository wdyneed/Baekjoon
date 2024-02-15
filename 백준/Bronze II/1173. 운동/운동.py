import sys

N, m, M, T, R = map(int, sys.stdin.readline().rstrip().split())

time = 0
temp_m = m

if m + T > M:
    time = -1
else:
    while (N > 0):
        if temp_m + T <= M:
            N -= 1
            temp_m += T
            time += 1
        else:
            if temp_m - R < m:
                temp_m = m
            else:
                temp_m -= R
            time += 1

print(time)
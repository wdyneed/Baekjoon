import sys

n = int(sys.stdin.readline())

dp = [1, 2, 3, 5]

for i in range(4, n):
    dp.append(dp[i - 1] + dp[i - 2])

print(dp[n - 1] % 10007)
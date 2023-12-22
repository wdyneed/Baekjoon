import sys

N = int(sys.stdin.readline())

# DP 초기화
dp = [[0]*10 for _ in range(N+1)]

# 1의 자리수 경우의 수 초기화
for i in range(1, 10):
    dp[1][i] = 1

MOD = 1000000000

for i in range(2, N+1):
    for j in range(10):
        #가장 뒤에 오는 수가 0일 땐 앞에 1만 올 수 있음
        if j == 0:
            dp[i][j] = dp[i-1][1]
        # 가장 뒤에 오는 숫자가 9일 땐 앞에 8만 올 수 있음
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        # 뒤에 오는 숫자가 1~8이면 앞에 +-1이 올 수 있음
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1] 

print(sum(dp[N]) % MOD)
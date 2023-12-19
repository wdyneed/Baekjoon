import sys

T = int(sys.stdin.readline())

def cal(N):
    dp = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12]
    
    if N <= len(dp):
        return dp[N - 1]
    
    else:
        j = 6
        for i in range(N - len(dp)):
            dp.append(dp[-1] + dp[j])
            j += 1
        return dp[N - 1]

for i in range(T):
    N = int(sys.stdin.readline())
    
    print(cal(N))
import sys

H, x = map(int, sys.stdin.readline().split())
m = 1
result = 0

for i in range(H):
    snow_cnt = int(sys.stdin.readline())
    m *= x
    m %= (10 ** 9 + 7)
    result += (snow_cnt * m)
    
    
print((result) % (10 ** 9 + 7))

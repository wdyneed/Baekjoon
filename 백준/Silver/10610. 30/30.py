import sys

N = sys.stdin.readline().rstrip()

N = sorted(N, reverse=True)

result = 0
    
if '0' in N:
    for i in N:
        result += int(i)
    if result % 3 != 0:
        print(-1)
    else:
        print(''.join(N))
else:
    print(-1)
import sys

def pow(a,b,c):
    if b == 1:
        return a % c
    
    n = pow(a,b//2,c)
    temp = n * n
    if b%2 == 0:
        return temp % c
    else:
        return a * temp % c

a,b,c = map(int,sys.stdin.readline().split())

ans = pow(a,b,c)
print(ans)
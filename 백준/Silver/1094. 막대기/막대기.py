import sys

a = int(sys.stdin.readline())

cnt = 0

while a != 0:
    if a % 2 == 1:
        cnt += 1
    a //= 2
    
print(cnt)
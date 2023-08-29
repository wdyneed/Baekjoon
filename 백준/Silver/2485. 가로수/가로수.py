import sys

N = int(sys.stdin.readline())

tree = []
for i in range(N):
    tree.append(int(sys.stdin.readline()))
    
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

maxdist = 0

for i in range(1, N):
    dist = tree[i] - tree[i - 1]
    maxdist = gcd(maxdist, dist)
    
cnt = 0

for i in range(1, N):
    cnt += (tree[i] - tree[i - 1]) // maxdist - 1
    
print(cnt)
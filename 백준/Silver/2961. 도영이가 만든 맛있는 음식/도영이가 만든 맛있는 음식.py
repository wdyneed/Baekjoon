import sys
from itertools import combinations

N = int(sys.stdin.readline())

arr = []

for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))
    
comb = []

for i in range(1, N + 1):
    comb.append(combinations(arr, i))

minvalue = 10000000000000001

for i in comb:
    for j in i:
        sour = 1
        bitter = 0
        for k in j:
            sour *= k[0]
            bitter += k[1]
        
        minvalue = min(minvalue, abs(sour - bitter))
        
print(minvalue)
            
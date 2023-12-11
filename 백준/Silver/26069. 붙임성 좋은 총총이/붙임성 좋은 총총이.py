import sys

N = int(sys.stdin.readline())
dance = ["ChongChong"]

for i in range(N):
    A, B = sys.stdin.readline().split()
    if A in dance:
        dance.append(B)
    if B in dance:
        dance.append(A)
    
print(len(set(dance)))
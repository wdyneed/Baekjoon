import sys

N = int(sys.stdin.readline().rstrip())
k = []

for i in range(N):
    k.append(int(sys.stdin.readline()))

k.sort()

result = []
p = 0
cnt = len(k)

for i in k:
    sum = 0
    sum = i * cnt
    result.append(sum)
    cnt -= 1

print(max(result))
             
import sys

N, K = map(int, sys.stdin.readline().split())

people = [i for i in range(1, N + 1)]
result = []
    
idx = 0

while people:
    idx = (idx + K - 1) % len(people)
    temp = people.pop(idx)
    result.append(temp)
    
print('<', end='')
for i in range(N - 1):
    print(result[i], end=', ')
print(result[-1], end='')
print('>', end='')
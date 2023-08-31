import sys

arr = []
count = 0

for i in range(8):
    arr.append(sys.stdin.readline().rstrip())
    for j in range(8):
        if i % 2 == 1 and j % 2 == 1 and arr[i][j] == 'F':
            count += 1
        if i % 2 == 0 and j % 2 == 0 and arr[i][j] =='F':
            count += 1
print(count)
max = 0
sum = 0

N = int(input())
arr = list(map(int, input().split()))

for i in range(0, N):
    if max < arr[i]:
        max = arr[i]
        
for i in range(0, N):
    arr[i] = arr[i] / max * 100
    sum += arr[i]

di = sum / N
print(di)
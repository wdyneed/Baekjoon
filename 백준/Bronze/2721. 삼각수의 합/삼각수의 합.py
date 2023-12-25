import sys

T = int(sys.stdin.readline())

arr = [0] * 301

for i in range(301):
    temp = 0
    for j in range(1, i + 3):
        temp += j
        
    arr[i] = (i + 1) * (temp)
    

for i in range(T):
    n = int(sys.stdin.readline())
    result = 0
    for j in range(n):
        result += arr[j]
    
    print(result)
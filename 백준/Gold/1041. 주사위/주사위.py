import sys

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

result = 0

min_list = []
if N == 1:
    arr.sort()
    for i in range(5):
        result += arr[i]

else:
    min_list.append(min(arr[0], arr[5]))
    min_list.append(min(arr[1], arr[4]))
    min_list.append(min(arr[2], arr[3]))
    min_list.sort()
    
    min1 = min_list[0]
    min2 = min_list[0] + min_list[1]
    min3 = sum(min_list)
    
    n1 = 4 * (N - 2) * (N - 1) + (N - 2) ** 2
    n2 = 4 * (N - 1) + 4 * (N - 2)
    n3 = 4
    
    result += min1 * n1
    result += min2 * n2
    result += min3 * n3

print(result)
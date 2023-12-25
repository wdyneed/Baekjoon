import sys

n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
x = int(sys.stdin.readline())

start = 0
count = 0
end = n - 1

while start < end:
    result_sum = arr[start] + arr[end]
    if result_sum > x:
        end -= 1
    elif result_sum < x:
        start += 1
    else:
        count += 1
        start += 1
        
print(count)
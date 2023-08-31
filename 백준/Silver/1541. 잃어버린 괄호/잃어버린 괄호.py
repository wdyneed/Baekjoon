import sys

str = sys.stdin.readline().rstrip().split('-')
arr = []
sumval = 1e9

for i in range(len(str)):
    temp = 0
    arr = str[i].split('+')
    
    for j in range(len(arr)):
        temp += int(arr[j])
        
    if sumval == 1e9:
        sumval = temp
        
    else:
        sumval -= temp
        
print(sumval)
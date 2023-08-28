import sys

N = int(sys.stdin.readline())
sumval = 0
three = 0

for i in range(1, N + 1):
    sumval += i
    three += i ** 3
    
print(sumval)
print(sumval ** 2)
print(three)

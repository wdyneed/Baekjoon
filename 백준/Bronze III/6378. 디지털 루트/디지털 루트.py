import sys

def digitalRoute(n):
    while(True):
        if len(str(n)) == 1:
            return n
        else:
            result = 0
            for i in str(n):
                result += int(i)
                n = result
            

while(True):
    number = int(sys.stdin.readline().rstrip())
    if number == 0:
        break
    print(digitalRoute(number))

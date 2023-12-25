import sys

S = []

M = int(sys.stdin.readline())

for i in range(M):
    program = sys.stdin.readline().rstrip().split()
    
    if len(program) == 1:
        if program[0] == "all":
            S = [i for i in range(1, 21)]
        else:
            S = []
        
    else:
        order, num = program[0], int(program[1])
        if order == "add":
            if num in S:
                continue
            else:
                S.append(num)
        
        elif order == "remove":
            if num in S:  
                S.remove(num)
            else:
                continue
        
        elif order == "check":
            if num in S:
                print(1)
            else:
                print(0)
                
        elif order == "toggle":
            if num in S:
                S.remove(num)
            else:
                S.append(num)
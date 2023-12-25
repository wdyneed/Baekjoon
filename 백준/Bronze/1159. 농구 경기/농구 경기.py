import sys

N = int(sys.stdin.readline())

firstname = {}


for i in range(N):
    name = sys.stdin.readline().rstrip()
    
    if name[0] not in firstname:
        firstname[name[0]] = 1
    
    elif name[0] in firstname:
        firstname[name[0]] += 1
        

result = [key for key, value in firstname.items() if value >= 5]



if len(result) == 0:
    print("PREDAJA")
else:
    result.sort()
    for i in result:
        print(i, end='')
import sys

arr = []

for i in range(5):
    agentname = sys.stdin.readline().rstrip()
    
    if agentname.find("FBI") != -1:
        arr.append(i + 1)
    
if len(arr) == 0:
    print("HE GOT AWAY!")

else:
    print(*arr)
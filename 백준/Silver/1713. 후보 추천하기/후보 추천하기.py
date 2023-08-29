import sys

N = int(sys.stdin.readline())
recom = int(sys.stdin.readline())

recom_list = list(map(int, sys.stdin.readline().split()))
recom_cntlist = [0] * 101
q = []

for i in recom_list:
    idx = -1
    min_val = 1e9
    
    if i in q:
        recom_cntlist[i] += 1
    else:
        if len(q) < N:
            q.append(i)
        else:
            for j in range(len(q)):
                if recom_cntlist[q[j]] < min_val:
                    idx = j
                    min_val = recom_cntlist[q[j]]
            recom_cntlist[q[idx]] = 0
            q.pop(idx)
            q.append(i)
            
        
q.sort()

print(*q)
import sys

def parent(p, x):
    result = [x]
    while p[x]:
        result.append(p[x])
        x = p[x]
    return result


T = int(sys.stdin.readline())
for i in range(T):
    N = int(sys.stdin.readline())
    graph = [0] * (N + 1)
    for j in range(N - 1):
        A, B = map(int, sys.stdin.readline().split())
        graph[B] = A
    find_A, find_B = map(int, sys.stdin.readline().split())
    A_parent = parent(graph, find_A)
    B_parent = parent(graph, find_B)
    
    i, j = 0, 0
    if len(A_parent) > len(B_parent):
        i = len(A_parent) - len(B_parent)
        
    else:
        j = len(B_parent) - len(A_parent)
        
    while A_parent[i] != B_parent[j]:
        i += 1
        j += 1
    print(A_parent[i])
        

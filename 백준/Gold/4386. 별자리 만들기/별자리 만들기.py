import math
import sys

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def kruskal(edges, n):
    parent = [i for i in range(n)]
    edges.sort(key=lambda x: x[2])
    mst_cost = 0

    for edge in edges:
        a, b, cost = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            mst_cost += cost

    return mst_cost

n = int(sys.stdin.readline())
stars = []
edges = []

for _ in range(n):
    x, y = map(float, sys.stdin.readline().split())
    stars.append((x, y))

for i in range(n):
    for j in range(i+1, n):
        cost = distance(stars[i], stars[j])
        edges.append((i, j, cost))

result = kruskal(edges, n)
print('{:.2f}'.format(result))

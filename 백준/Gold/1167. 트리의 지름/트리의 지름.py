import sys
sys.setrecursionlimit(10**5)

V = int(sys.stdin.readline())

graph = [[] * V for _ in range(V + 1)]
visited_dfs = [-1] * (V + 1)

def dfs(node, weight):
    # 원하는 노드에서 다른 노드들(ex:1번 노드에서 나머지 노드들)까지의 거리 구하는 함수
    for n, l in graph[node]:
        cost = weight + l
        # 방문을 하지 않았다면, 가중치 저장
        if visited_dfs[n] == -1:
            visited_dfs[n] = cost
            dfs(n, cost)
    return


for i in range(1, V + 1):
    nodeinfo = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(1, len(nodeinfo), 2):
        if nodeinfo[j] == -1:
            continue
        else:
            graph[nodeinfo[0]].append((nodeinfo[j], nodeinfo[j + 1]))

        
visited_dfs[1] = 0

dfs(1, 0)
# 노드 1에서 시작해서 가장 먼 노드 찾기(인덱스)
idx = visited_dfs.index(max(visited_dfs))

# 방문 리스트 초기화
visited_dfs = [-1] * (V + 1)
visited_dfs[idx] = 0

# 임의의 노드에서 가장 먼 노드를 찾고 거기서 가장 먼 노드를 찾으면 그것이 트리의 지름
dfs(idx, 0)

print(max(visited_dfs))
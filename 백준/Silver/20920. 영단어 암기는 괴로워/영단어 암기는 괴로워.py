import sys

N, M = map(int, sys.stdin.readline().split())

voca_dict = {}

for i in range(N):
    voca = sys.stdin.readline().rstrip()
    if len(voca) >= M:
        if voca in voca_dict:
            voca_dict[voca] += 1
        else:
            voca_dict[voca] = 1    
    
sorted_items = sorted(voca_dict.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for key, value in sorted_items:
    print(key)
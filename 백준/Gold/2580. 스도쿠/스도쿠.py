import sys

arr = []
# 배열 입력받기
blank = []
# 배열 빈칸(0)을 x, y 좌표로 입력받음

for i in range(9):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))
    
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            # 빈 칸 추가
            blank.append((i, j))
            
def checkrow(x, a):
    # 행에서 존재하지 않는 값 찾기
    for i in range(9):
        if a == arr[x][i]:
            return False
    return True

def checkcol(y, a):
    # 열에서 존재하지 않는 값 찾기
    for i in range(9):
        if a == arr[i][y]:
            return False
    return True

def checkthreebythree(x, y, a):
    # 3 * 3 칸에서 값 찾기
    dividex = x // 3 * 3
    dividey = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if a == arr[dividex + i][dividey + j]:
                return False
    return True

def dfs(idx):
    if idx == len(blank):
        for i in range(9):
            print(*arr[i])
        exit(0)
    
    for i in range(1, 10):
        x = blank[idx][0]
        y = blank[idx][1]
        
        if checkrow(x, i) and checkcol(y, i) and checkthreebythree(x, y, i):
            arr[x][y] = i
            dfs(idx + 1)
            arr[x][y] = 0
            
dfs(0)
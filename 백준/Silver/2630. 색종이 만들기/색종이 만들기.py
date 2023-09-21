import sys


N = int(sys.stdin.readline())
arr = []

for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

result = []

def colorpaper(x, y, n):
    color = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != arr[i][j]:
                # n이 8일 경우
                # x:0~4 y: 0~4 왼쪽 상단
                colorpaper(x, y, n // 2)
                # x: 0~4 y: 4 ~ 8 왼쪽 하단
                colorpaper(x, y + n // 2, n // 2)
                # x : 4~8 y: 0~4 우측 상단
                colorpaper(x+n//2, y, n//2)
                # x: 4~8 y: 4~8 우측 하단
                colorpaper(x+n//2, y+n//2, n//2)
                return
    # 색깔이 전부 같을 때
    if color == 0:
        result.append(0)
    else:
        result.append(1)

colorpaper(0, 0, N)
print(result.count(0))
print(result.count(1))
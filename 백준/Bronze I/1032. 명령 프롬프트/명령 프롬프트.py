import sys

N = int(sys.stdin.readline())
arr = []

for i in range(N):
    arr.append(sys.stdin.readline().rstrip())
    
word_len = len(arr[0])
result = list(arr[0])

for i in range(N):
    for j in range(i + 1, N):
        for k in range(word_len):
            if arr[i][k] == arr[j][k]:
                continue
            else:
                result[k] = '?'
                
print(''.join(result))
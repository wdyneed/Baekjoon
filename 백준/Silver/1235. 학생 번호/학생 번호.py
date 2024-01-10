import sys

N = int(sys.stdin.readline())
student_num = []
count = 0

for i in range(N):
    student_num.append(sys.stdin.readline().rstrip())

student_numlen = len(student_num[0])

for i in range(student_numlen - 1, -1, -1):
    temp_num = []
    for j in student_num:
        temp_num.append(j[i:])
    count += 1
    if len(temp_num) != len(set(temp_num)):
        continue
    else:
        break
        
print(count)
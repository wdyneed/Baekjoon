import sys

switch_num = int(sys.stdin.readline())

switch = [-1] + list(map(int, sys.stdin.readline().split()))

student_num = int(sys.stdin.readline())

def change(x):
    global switch
    switch[x] = abs(switch[x]-1)


for _ in range(student_num):
    gender, no = map(int, sys.stdin.readline().split())
    i = 1
    # 남자일 때
    if gender == 1:
        while no * i <= switch_num:
            change(no * i)
            i += 1
    # 여자일 때
    elif gender == 2:
        change(no)
        while 1 <= no-i and no+i <= switch_num and switch[no-i] == switch[no+i]:
            change(no-i)
            change(no+i)
            i += 1
            
for i in range(1, switch_num + 1):
    print(switch[i], end = ' ')
    if not i % 20:
        print()
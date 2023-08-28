import sys

N = sys.stdin.readline().rstrip()

if N == 'M':
    print('MatKor')
    
elif N == 'W':
    print('WiCys')

elif N == 'C':
    print('CyKor')

elif N == 'A':
    print('AlKor')
    
else:
    print('$clear')
import sys
from collections import deque

n = int(input())
que = deque()

for i in range(n):
    c = sys.stdin.readline().split()
    if c[0] == 'push':
        que.append(c[1])
    elif c[0] == 'pop':
        if len(que) != 0:
            print(que.popleft())
        else:
            print(-1)
    elif c[0] == 'size':
        print(len(que))
    elif c[0] == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif c[0] == 'front':
        if len(que) !=0:
            print(que[0])
        else:
            print(-1)
    elif c[0] == 'back':
        if len(que) !=0:
            print(que[-1])
        else:
            print(-1)

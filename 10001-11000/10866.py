import sys
from collections import deque
stack = deque()
n = int(input())

for i in range(n):
    c = sys.stdin.readline().split()
    if c[0] == 'push_back':
        stack.append(c[1])
    elif c[0] == 'push_front':
        stack.insert(0,c[1])
    elif c[0] == 'pop_front':
        if len(stack) != 0:
            print(stack.popleft())
        else:
            print(-1)
    elif c[0] == 'pop_back':
        if len(stack) != 0:
            print(stack.pop())
        else:
            print(-1)
    elif c[0] == 'size':
        print(len(stack))
    elif c[0] == 'empty':
        if len(stack) != 0:
            print(0)
        else:
            print(1)
    elif c[0] == 'front':
        if len(stack) != 0:
            print(stack[0])
        else:
            print(-1)
    elif c[0] == 'back':
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)





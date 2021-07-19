# 문제번호:10828
# 문제이름: 스택
import sys

n = int(sys.stdin.readline()) # 명령의 수
stack = []

def push(a):
    stack.append(a)

def pop():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])
        stack.pop()

def size():
    print(len(stack))

def empty():
    if len(stack)==0:
        print(1)
    else:
        print(0)

def top():
    if len(stack)==0:
        print(-1)
    else:
        print(stack[-1])

for i in range(n):

    a = sys.stdin.readline().split()

    if len(a)==1:
        c = a[0]
        if c == 'pop':
            pop()
        elif c == 'size':
            size()
        elif c == 'empty':
            empty()
        elif c == 'top':
            top()
    else:
        c = a[0]
        b = int(a[1])
        if c == 'push':
            push(b)







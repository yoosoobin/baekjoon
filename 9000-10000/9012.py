# 문제번호: 9012
# 문제이름: 괄호

def solve():
    data = input()
    stack = []
    for item in data:
        if item == '(':
            stack.append(item)
        else:
            if len(stack) == 0:
                print('NO')
                return
            else:
                stack.pop()
    if len(stack)==0:
        print('YES')
    else:
        print('NO')

t = int(input())
for _ in range(t):
    solve()











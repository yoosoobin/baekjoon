# 문제번호: 9093
# 문제이름: 단어 뒤집기
import sys

t = int(sys.stdin.readline())

for i in range(t):
    sent = sys.stdin.readline().split()
    for j in sent:
        for h in range(len(j)-1,-1,-1):
            print(j[h], end='')
        print(end=' ')


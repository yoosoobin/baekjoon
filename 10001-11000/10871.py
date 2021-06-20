# X보다 작은 수
N, X = map(int, input().split())
list = input().split()
for i in range(0, N):
    if int(list[i]) < X:
        print(list[i], end=' ')



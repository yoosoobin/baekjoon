'''
번호: 10818
제목: 최소, 최대
'''
n = int(input())
arr = list(map(int, input().split()))
max = -1000000
min = 1000000
for i in range(n):
    fir = arr[i]
    if fir >= max:
        max = fir
    if fir <= min:
        min = fir
print(min,max)
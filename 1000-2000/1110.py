'''
번호: 1110
제목: 더하기 사이클
'''
N = int(input())
ori = N
count = 0
while True:
    if N<10:
        N=N*10
        a=N//10
        b=N%10
        N= a*10+(a+b)%10
        count += 1
    else:
        a = N // 10
        b = N % 10
        N= b*10+(a+b)%10
        count += 1
    if N == ori:
        print(count)
        break


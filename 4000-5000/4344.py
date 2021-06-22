'''
번호: 4344
제목: 평균은 넘겠지
'''
N = int(input())

for _ in range(N):
    sum = 0
    cnt = 0
    n_list = list(map(int, input().split()))
    for i in range(1,n_list[0]+1) :
        sum += n_list[i]
    avg = sum/n_list[0]
    for i in range(1, n_list[0] + 1):
        if n_list[i] > avg:
            cnt += 1
    per = round((cnt / n_list[0]) * 100,3)
    print("{0:0.3f}".format(per),"%",sep='')
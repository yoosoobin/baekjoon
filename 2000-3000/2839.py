#문제번호: 2839
#알고리즘: 그리디
#문제이름: 설탕 배달

n = int(input())
cnt = 0
while True:
    if n%5 ==0:
        cnt+=n//5
        print(cnt)
        break
    else:
        n -= 3
        cnt+=1

    if n==0:
        print(cnt)
        break
    elif n<0:
        print(-1)
        break
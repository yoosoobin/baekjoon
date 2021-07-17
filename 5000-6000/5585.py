# 문제번호: 5585
# 알고리즘: 그리디
# 문제이름: 거스름돈
n = 1000-int(input())

m_list = [500,100,50,10,5,1]
cnt = 0
for i in m_list:
    cnt += n//i
    n %= i

print(cnt)
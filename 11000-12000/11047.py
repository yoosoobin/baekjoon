# 문제번호: 11047
# 알고리즘: 그리디
# 문제이름: 동전0
n,k = map(int,input().split())
c_list = []
for i in range(n):
    c_list.append(int(input()))
c_list.sort(reverse=True)

cnt=0
for i in c_list:
    cnt += k//i
    k %= i
print(cnt)
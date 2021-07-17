# 문제번호: 10162
# 알고리즘: 그리디
# 문제이름: 전자레인지

t = int(input())

s_list = [300, 60, 10]

cnt = []

if t%10 != 0:
    print(-1)
else:
    for i in s_list:
        cnt.append(t//i)
        t %= i

for i in cnt:
    print(i,end=' ')
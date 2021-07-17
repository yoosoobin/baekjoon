#문제번호:2720
#알고리즘:그리디
#문제이름:세탁소 사장 동혁

n = int(input())
coin_list = [25,10,5,1]
m=[]
for i in range(n):
    m.append(int(input()))

for i in m:
    cnt=[]
    for j in coin_list:
        cnt.append(i//j)
        i %= j

    for s in cnt:
        print(s , end=' ')
    print()

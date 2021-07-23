n = int(input())

num_list = list(map(int,input().split()))

ans = 0
x=True

for num in num_list:
    s = 2
    if num ==1:
        continue
    elif num in (2,3):
        ans +=1
    else:
        o = int((num**0.5))
        while s<=(num**0.5):
            if num%s == 0:
                break
            else:
                s += 1
        if s==o+1:
            ans+=1



print(ans)


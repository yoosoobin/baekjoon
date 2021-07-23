n = int(input())

def pac(n):
    ans = 1
    for i in range(1,n+1):
        ans *= i
    return ans

num = str(pac(n))

cnt =0

for i in range(len(num)-1,0-1,-1):
    if num[i] == '0':
        cnt += 1

    else:
        print(cnt)
        break


a,b = map(int, input().split())

def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)

def lcd(a,b):
    if a%b==0:
        return a
    else:
        g = gcd(a,b)
        return(g*(a//g)*(b//g))

print(gcd(a,b))
print(lcd(a,b))
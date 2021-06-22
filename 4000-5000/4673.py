'''
번호: 4673
제목: 셀프 넘버
'''
def d():
    not_self = []
    for i in range(1, 10001):
        num = i
        for j in str(i):
            num += int(j)
        not_self.append(num)
    for n in range(1, 10001):
        if n not in not_self:
            print(n)
d()

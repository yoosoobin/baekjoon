'''
번호 : 2577
제목 : 숫자의 개수
'''
A = int(input())
B = int(input())
C = int(input())
mul = str(A*B*C)
zero = 0
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
seven = 0
eight = 0
nine = 0

for i in range(len(mul)):
    if mul[i] == '0':
        zero += 1
    elif mul[i] =='1':
        one += 1
    elif mul[i] =='2':
        two += 1
    elif mul[i] =='3':
        three += 1
    elif mul[i] =='4':
        four += 1
    elif mul[i] =='5':
        five += 1
    elif mul[i] =='6':
        six += 1
    elif mul[i] =='7':
        seven += 1
    elif mul[i] =='8':
        eight += 1
    elif mul[i] =='9':
        nine += 1
print(zero,one,two,three,four,five,six,seven,eight,nine,sep='\n')





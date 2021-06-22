'''
번호: 1546
제목: 평균
'''
n = int(input())
score = list(map(int,input().split()))
max=0
for s in score:
    if s > max:
        max = s

new_score = 0

for s in score:
    s = s/max*100
    new_score += s

print(new_score/n)



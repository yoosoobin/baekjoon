'''
번호: 10952
제목: A+B-5
설명: 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
'''
import sys

while True:
    A, B = map(int, sys.stdin.readline().rstrip('\n').split())
    if A==0 and B==0:
        break
    print(A + B)




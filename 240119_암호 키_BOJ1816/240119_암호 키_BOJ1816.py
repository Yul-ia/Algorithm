# 240118_암호 키
import sys
sys.stdin=open('input.txt')
input = sys.stdin.readline

N = int(input())

for i in range(N):
    s =int(input())
    for j in range(2,10**6+1):
        if s % j == 0:
            print('NO')
            break
        else:
            pass
    else:
        print('YES')


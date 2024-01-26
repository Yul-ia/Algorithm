# 240117_수학은 비대면 강의 입니다.

import sys
sys.stdin=open('input.txt')
input = sys.stdin.readline

a,b,c,d,e,f = map(int,input().split())

for x in range(-999,1000):
    for y in range(-999,1000):
        if 0 == a * x + b * y - c :
            if 0 == d * x + e * y - f :
                print(x, y)
                quit()
# 세탁소 사장 동혁_BOJ2720

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

t= int(input())
q = 25
d = 10
n = 5
p = 1

for i in range(t):
    re = int(input())
    a = int(re//q)
    b = int((re-a*q)//d)
    c = int((re-a*q-b*d)//n)
    e = int((re-a*q-b*d-c*n)//p)

    print(a,b,c,e)
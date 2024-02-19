# 뜨거운 붕어빵_BOJ11945

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

r =[]
s=''
n,m = map(int,input().split())
for i in range(n):
    o = list(input().strip())
    o.reverse()
    # print(o)
    s = ''
    for j in o:
        s+=j
    print(s)
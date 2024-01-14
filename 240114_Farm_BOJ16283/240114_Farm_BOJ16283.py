# Farm_BOJ16283

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

a,b,n,w = map(int,input().split())

temp =[]
for A in range(1,n+1): # 한 마리 이상, 최대 n마리
    if a*A + b*(n-A) == w and A !=n :
        temp.append(A)


if not temp:
    print(-1)
elif len(temp)>=2:
    print(-1)
else:
    print(temp[0], n-temp[0])



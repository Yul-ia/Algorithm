# 240126_2차원 배열의 합

import sys
sys.stdin=open('input.txt')
input = sys.stdin.readline

N,M = map(int,input().split())
lst =[]
for i in range(N):
    A = list(map(int,input().split()))
    lst.append(A)

k = int(input())
for _ in range(k):
    cnt = 0
    i, j , x, y = map(int,input().split())
    for k in range(i-1,x):
        for f in range(j-1,y):
            cnt += lst[k][f]
    print(cnt)

# 블랙잭_BOJ2798

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int,input().split()) # N장의 카드, 세장의 카드 합이 M을 넘으면 안돼
card = list(map(int, input().split())) # N장의 카드

lst = []

for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            Sum=card[i]+card[j]+card[k]
            if Sum <= M: # M을 넘지 않으면서 = M 이하
                lst.append(Sum)
            else:
                pass

print(max(lst))

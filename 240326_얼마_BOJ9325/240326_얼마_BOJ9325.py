# 얼마_BOJ9325
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = int(input()) # 자동차 가격
    n = int(input()) # 옵션 개수

    cnt = 0
    for _ in range(n):
        q,p = map(int,input().split()) # 옵션 개수, 옵션가격
        cnt += q*p
    print(cnt+s)


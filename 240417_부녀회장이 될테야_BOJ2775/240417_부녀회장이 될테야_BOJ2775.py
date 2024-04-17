# 부녀회장이 될테야_BOJ2775

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

t=int(input())
for _ in range(t):
  k = int(input()) #층
  n = int(input()) #호
  zero = []
  for p in range(1,n+1): #0층의 호
    zero.append(p)
  #[1,2,3,..n]

  for i in range(k):#반복 횟수, 층수 만큼 반복
    ho_cnt = 0
    for j in range(n):
      ho_cnt +=zero[j]
      zero[j]=ho_cnt
    # print(i,zero)
  print(zero[-1])

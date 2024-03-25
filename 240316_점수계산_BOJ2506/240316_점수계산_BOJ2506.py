# 점수계산_BOJ2506
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))
score = [0]*n
cnt =0

for i in range(0,n):
    if lst[i] ==1:
        cnt +=1
        score[i]=cnt
    else:
        cnt =0
        score[i]=cnt

print(sum(score))
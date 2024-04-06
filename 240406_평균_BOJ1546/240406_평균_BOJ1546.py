# 평균_BOJ1546
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
lst = list(map(float,input().split()))
m = max(lst)

new=[]
for i in lst:
    new.append(i/m*100)

print(round((sum(new)/n),6))
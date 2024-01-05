# 회전하는 큐_BOJ1021

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

#queue
from collections import  deque
que = deque()

n,m = map(int,input().split())
l1 = list(map(int, input().split()))
for i in range(1, n+1):
    que.append(i)
print(que)



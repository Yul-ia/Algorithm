# 회전하는 큐_BOJ1021

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


from collections import  deque
que = deque()

n,m = map(int,input().split())
location = list(map(int, input().split())) #location
for i in range(1, n+1):
    que.append(i)

count = 0

for j in location:
    while True:
        if que[0] == j:
            que.popleft()
            break
        else:
            if que.index(j) > (len(que)//2):
                que.rotate(1) # 문제 3번수행
                count +=1
            elif que.index(j) <= (len(que)//2):
                que.rotate(-1) # 문제 2번수행
                count += 1

print(count)


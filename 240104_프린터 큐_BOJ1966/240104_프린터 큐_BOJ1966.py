# 프린터 큐 _BOJ1966

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque #Queue

T = int(input())
for i in range(T):
    n, m = map(int, input().split()) # 문서의 개수, 현재 몇 번째
    lst = list(map(int, input().split())) # 중요도/맨 왼쪽 0번째

    count = 0

    que = deque()
    for i in range(n):
        que.append([lst[i], i])

    while True:
        if que[0][0] >= max(que)[0]:
            temp = que.popleft()
            count += 1
            if temp[1] == m:
                break
        else:
            que.rotate(-1)
    print(count)





# 프린터 큐 _BOJ1966

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline()

T = int(input)
from collections import deque #Queue
queue = deque()

for i in range(T):
    n,m =map(int,input.split()) # 문서의 개수, 현재 몇 번째
    importance = list(map(int,input.split())) # 중요도/맨 왼쪽 0번째
    importance_que = deque(importance)
    if


  #
  # 119111
  # 012345
  # queue.popleft()




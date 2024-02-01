# 킹, 퀸, 룩, 비숍, 나이트, 폰 _BOJ3003

import sys
sys.stdin =open('input.txt')
input = sys.stdin.readline

chess = [1,1,2,2,2,8]
lst = list(map(int,input().split()))
result = []
for i in range(6):
    x = chess[i]-lst[i]
    result.append(x)
print(*result)



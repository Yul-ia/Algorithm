# 369_BOJ17614

import sys
sys.stdin = open('input.txt')
input=sys.stdin.readline

N = int(input().strip())
cnt = 0
for i in range(1,N+1):
    for j in str(i):
        if j == '3' or j == '6' or j == '9':
            cnt +=1
        else:
            pass
print(cnt)

# 세로읽기_BOJ10798

import sys
sys.stdin=open('input.txt')
input = sys.stdin.readline

lst =[]
for _ in range(5):
    T = list(input().strip())
    lst.append(T)

String = []
for i in range(len(T)):
    for j in range(len(lst)):
         if len(lst[j]) > i:
              String.append(lst[j][i])
ans =''
for s in String:
    ans += s
print(ans)
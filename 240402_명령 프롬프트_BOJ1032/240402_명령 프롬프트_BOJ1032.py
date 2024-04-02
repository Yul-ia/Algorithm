# 명령 프롬프트_BOJ1032

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

lst=[]
n= int(input())
for _ in range(n):
    s = input().strip()
    lst.append(s)

fst = lst[0]
for i in lst:
    same = ''
    for j in range(len(fst)):
        if fst[j]==i[j]: #알파벳 하나씩 확인
            same += fst[j]
        else:
            same += '?'
    fst = same
print(same)


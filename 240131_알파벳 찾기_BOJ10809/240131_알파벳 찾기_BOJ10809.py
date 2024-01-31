# 알파벳 찾기_BOJ10809

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

s = list(input())

alpha = 'abcdefghijklmnopqrstuvwxyz'
lst = []
for i in alpha:
    if i in s:
        lst.append(s.index(i))
    else:
        lst.append(-1)
print(*lst)


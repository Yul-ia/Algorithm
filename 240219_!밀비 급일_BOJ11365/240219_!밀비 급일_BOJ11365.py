# !밀비 급일_BOJ11365

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

while True:
    s = list(input().strip())
    if s[0]=='E' and s[1]=='N' and s[2]=='D':
        break
    s.reverse()
    w = ''
    for i in s:
        w+=i
    print(w)
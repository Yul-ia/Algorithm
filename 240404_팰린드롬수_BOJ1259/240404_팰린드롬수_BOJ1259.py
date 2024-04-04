# 팰린드롬수_BOJ1259

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

while True:
    s = input().strip()
    if s == '0':
        break
    N =len(s)
    for i in range(N//2):
        if s[i] != s[N-i-1]:
            print("no")
            break
    else: print("yes")

# Dedupe_BOJ5357

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    s = ''
    data = input().strip()
    for i in data:
        if s == '' or s[-1] != i:
            s += i
    print(s)


# 그게 무슨 코드니.._BOJ31495

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

s = input().strip()
result = ''

if s[0] == '\"' and s[-1] == '\"':
    for i in s:
        if i != '\"' or i !='\"':
            result+=i
    if result == '':
        print("CE")
    else:
        print(result)
else:
    print("CE")
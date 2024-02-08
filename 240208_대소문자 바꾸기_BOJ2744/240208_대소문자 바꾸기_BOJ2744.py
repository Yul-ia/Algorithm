# 대소문자 바꾸기_BOJ2744

import sys
sys.stdin=open('input.txt')
input = sys.stdin.readline

eng = input()
s = ''
for i in eng:
    if i.islower(): #.isupper()
        s += i.upper()
    else:
        s += i.lower()
print(s)
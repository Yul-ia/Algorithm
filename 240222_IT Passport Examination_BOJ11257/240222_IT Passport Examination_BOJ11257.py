#IT Passport Examination_BOJ11257

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    s = input().split()
    lst =[int(s[1]),int(s[2]),int(s[3])]
    total = lst[0] + lst[1] + lst[2]
    if lst[0]/35>=0.3 and lst[1]/25>=0.3 and lst[2]/40>=0.3:
        if total>=55:
            print(s[0],total, "PASS")
        else:
            total = lst[0]+lst[1]+lst[2]
            print(s[0], total, "FAIL")
    else:
        print(s[0], total, "FAIL")

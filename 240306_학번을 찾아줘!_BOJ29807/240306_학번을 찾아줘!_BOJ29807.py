# 학번을 찾아줘!_BOJ29807

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input()) # 국어, 수학, 영어, 탐구, 제2외국어
lst = list(map(int,input().split()))

hac = 0
if n > 0 and n < 3:
    hac += lst[0]*508

if n > 1 and n < 4: # n=2 국어 수학
    hac += lst[1]*212

if n > 2: # n=3 국어 수학 영어
    if lst[0] > lst[2]:  # 국어 > 영어
        hac += (lst[0]-lst[2])*508
    else:
        hac += abs(lst[0] - lst[2]) * 108

if n > 3: # n=4 국어 수학 영어 탐구
    if lst[1]>lst[3]: # 수학 > 탐구
        hac += (lst[1]-lst[3])*212
    else:
        hac += abs(lst[1] - lst[3]) * 305

if n > 4:
    hac += lst[4] * 707

print(hac*4763)
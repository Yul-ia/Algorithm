# 통학의 신_BOJ17945

# input.txt 열기
# import math
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

A,B = map(int,input().split())

T1 = -A + (A**2-B)**0.5
T2 = -A - (A**2-B)**0.5


lst =[]
if A**2==B: # 짝수 중근 판별
    print(int(T1))

else:
    lst.append(int(T1))
    lst.append(int(T2))
    lst.sort()

    print(*lst)

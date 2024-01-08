# 통학의 신_BOJ17945

# input.txt 열기
import math
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

A,B = map(int,input().split())

T1 = -A + math.sqrt(A**2-B)
T2 = -A - math.sqrt(A**2-B)
lst =[]
if A**2==B:
    print(T1)
else:
    lst.append(T1)
    lst.append(T2)
    lst.sort()

print(lst)


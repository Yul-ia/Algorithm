# 이진수_BOJ3460
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    lst = []
    while n > 0:
        lst.append(n % 2)
        n = n//2

    result = []
    cnt=0
    for i in lst:
        cnt += 1
        if i ==1:
            result.append(cnt-1)

    for j in result:
        print(j,end=' ')

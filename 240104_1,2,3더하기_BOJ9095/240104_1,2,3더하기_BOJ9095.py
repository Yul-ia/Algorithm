# 1,2,3 더하기_BOJ9095

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())

for i in range(T):
    n = int(input())
    t = [0]*(n+1)
    for j in range(n+1):
        if j == 1:
            t[j] = 1
        elif j == 2:
            t[j] = 2
        elif j == 3:
            t[j] = 4
        elif j >= 4:
            t[j] = t[j-1] + t[j-2] + t[j-3]
    print(t[-1])


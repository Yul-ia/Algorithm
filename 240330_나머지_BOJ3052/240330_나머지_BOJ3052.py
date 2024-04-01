# 나머지_BOJ3052
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

lst = []
for _ in range(10):
    n = int(input())
    if n%42 not in lst:
        lst.append(n%42)
print(len(lst))


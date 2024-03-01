# 특별한 작은 분수_BOJ27890
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

x,n = map(int,input().split())

for _ in range(n):
    if x % 2 !=0:
        x = (2*x)^6
    else:
        x= (x//2)^6
print(x)
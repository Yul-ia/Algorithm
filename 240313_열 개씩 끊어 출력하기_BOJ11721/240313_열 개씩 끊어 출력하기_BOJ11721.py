# 열 개씩 끊어 출력하기_BOJ11721
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

s =input().strip()

n = len(s) // 10 # 10개씩 끊어
last = len(s)%10 # 마지막

for _ in range(n):
    print(s[0:10])
    s = s[10:]

if last !=0:
    print(s[-last:])


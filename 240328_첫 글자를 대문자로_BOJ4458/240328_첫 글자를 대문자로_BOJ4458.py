# 첫 글자를 대문자로_BOJ4458
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    c = ''
    w = input().strip()
    c +=w[0].upper()
    c +=w[1:]
    print(c)

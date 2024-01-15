# 240115_완전제곱수

import sys
sys.stdin=open('input.txt')
input = sys.stdin.readline

N = int(input())
count = 0
for A in range(1,501):
    for B in range(1,A+1):
        if A**2 == (B**2)+N:
            count += 1
print(count)
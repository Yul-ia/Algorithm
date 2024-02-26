# Bicycle_BOJ20233

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# case a
a = int(input())
x = int(input())
# case b
b = int(input())
y = int(input())

t = int(input())

A = (((t-30)*x*21)+a)
B = (((t-45)*y*21)+b)
if t > 45:
    print(A,B)
elif t > 30 and t <= 45:
    print(A,b)
elif t <= 30:
    print(a,b)


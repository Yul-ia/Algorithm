# 수도요금_BOJ10707

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

x_charge = int(input())
y_charge = int(input())
c = int(input()) # 기본리터
plus_charge = int(input()) # 추가요금
user = int(input())

x_cnt = x_charge*user
y_cnt = y_charge
if user > c:
    y_cnt+=(user-c)*plus_charge

if x_cnt>=y_cnt:
    print(y_cnt)
else:
    print(x_cnt)


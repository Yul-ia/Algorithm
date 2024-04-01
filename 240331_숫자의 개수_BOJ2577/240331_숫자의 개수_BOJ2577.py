# 숫자의 개수_BOJ2577
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
cnt =1
for _ in range(3):
    a = int(input())
    cnt *= a

for i in range(10):
    num_cnt=0
    for j in str(cnt):
        if str(i) == j:
            num_cnt+=1
    print(num_cnt)